import json
from django.db.models import Count, Sum, Avg, Max
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404, get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
from usercenter.models import Department
from . import serializers
from . import models
from .filters import FlatDataFilterSet


class FlatDataViewSet(viewsets.ModelViewSet):
    queryset = models.FlatData.objects.order_by('pk')
    serializer_class = serializers.FlatDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FlatDataFilterSet


class FlatConfigViewSet(viewsets.ModelViewSet):
    queryset = models.FlatConfig.objects.order_by('pk')
    serializer_class = serializers.FlatConfigSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = serializers.FlatConfigSerializer.Meta.fields


class FlatTemplateViewSet(viewsets.ModelViewSet):
    queryset = models.FlatTemplate.objects.order_by('pk')
    serializer_class = serializers.FlatTemplateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'template_id',)


class FlatDataReportConfViewSet(viewsets.ModelViewSet):
    queryset = models.FlatDataReportConf.objects.order_by('pk')
    serializer_class = serializers.FlatDataReportConfSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sys_id', 'org_id', 'biz_id', 'report_id', 'flat_config',)


class FlatDataReportConfCopyView(viewsets.GenericViewSet):
    queryset = models.FlatDataReportConf.objects.order_by('pk')
    serializer_class = serializers.FlatDataReportConfSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.pk = None
        instance.report_id = (self.queryset.aggregate(max_report_id=Max('report_id'))['max_report_id'] or 0) + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FlatDataReportView(APIView):
    model = models.FlatDataReportConf
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def parse_json(self, conf_text):
        return json.loads(conf_text)

    def filter_queryset(self, qs, filter_conf):
        for key in filter_conf:
            if key in self.request.GET:
                qs = qs.filter(**{key: self.request.GET[key]})
        return qs

    def aggregate_func(self, value_type):
        value_type_dict = {
            'count': Count,
            'avg': Avg,
            'sum': Sum,
        }
        if value_type not in value_type_dict:
            raise ValueError('aggregate func type error')
        return value_type_dict[value_type]

    def distinct_count(self, qs, field_name):
        results = qs.values(field_name).annotate(count=Count(field_name)).order_by()
        data = {}
        for r in results:
            data[str(r[field_name])] = r['count']
        return data

    def distinct_sum(self, qs, field_name, target):
        results = qs.values(field_name).annotate(sum=Sum(target)).order_by()
        data = {}
        for r in results:
            data[str(r[field_name])] = r['sum']
        return data

    def aggregate(self, qs, aggregate_conf):
        special = ['distinct_count', 'distinct_sum',]
        result = {}
        for conf in aggregate_conf:
            func = conf['func']
            field = conf['field']
            output = conf.get('output', field)
            if func in special:
                if func == 'distinct_count':
                    r_data = self.distinct_count(qs, field)
                    for k in conf.get('keys', []):
                        r_data[str(k)] = r_data.get(str(k), 0)
                    result[output] = r_data
                elif func == 'distinct_sum':
                    r_data = self.distinct_sum(qs, field, conf['target'])
                    for k in conf.get('keys', []):
                        r_data[str(k)] = r_data.get(str(k), 0)
                    result[output] = r_data
            else:
                result[output] = qs.aggregate(**{field: self.aggregate_func(func)(field)})[field]
        return result

    def render_charts(self, data, conf):
        dd = {}
        aggregate_name = conf['aggregate_name']
        aggre_data = data[aggregate_name]
        name_map = conf.get('name_map')
        named_map = {}
        if name_map:
            if name_map['to'] == 'department':
                named_map = {str(i['id']): i['name'] for i in Department.objects.all().values('id', 'name')}
        for k, v in aggre_data.items():
            name = str(k)
            name = named_map.get(name, name)
            dd[name] = v
        return dd

    def header_clean_data(self, headers, data):
        result = []
        for d in data:
            r_data = {}
            for i in headers:
                r_data[i] = d[i]
            result.append(r_data)
        return result

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, report_id=kwargs['report_id'])
        flat_conf = obj.flat_config
        if flat_conf is None:
            flat_conf = get_list_or_404(models.FlatConfig, biz_id=obj.biz_id, org_id=obj.org_id, sys_id=obj.sys_id)[0]
        qs = models.FlatData.objects.filter(
            org_id=obj.org_id, sys_id=obj.sys_id, biz_id=obj.biz_id
        )
        arguments_conf = self.parse_json(obj.arguments)
        data_struct_conf = self.parse_json(obj.data_struct)
        charts_struct_conf = self.parse_json(obj.charts_struct)
        if not arguments_conf or not data_struct_conf or not charts_struct_conf:
            conf_header = serializers.FlatConfigSerializer(flat_conf).data
            header = {}
            for k, v in conf_header.items():
                if 'field' in k and v:
                    header[k] = v
            data = serializers.FlatDataSerializer(
                qs, many=True
            ).data
            return Response({'title': obj.report_name, 'header': header, 'data': self.header_clean_data(header, data)})
        qs = self.filter_queryset(qs, arguments_conf.get('filter', []))
        data = serializers.FlatDataSerializer(
            qs, many=True
        ).data
        header = data_struct_conf.get('header', {})
        result_dict = {'title': obj.report_name, 'header': header, 'data': self.header_clean_data(header, data)}
        if 'aggregate' in arguments_conf:
            aggregates = self.aggregate(qs, arguments_conf['aggregate'])
            result_dict['aggreate'] = aggregates
        if charts_struct_conf:
            charts = self.render_charts(result_dict.get('aggreate', {}), charts_struct_conf)
            result_dict['charts'] = charts
        return Response(result_dict)
