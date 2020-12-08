import json
from django.db.models import Count, Sum, Avg, Max, Min
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404, get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
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
    lookup_field = 'report_id'
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


def dictfetchall(sql, *args):
    """Returns all rows from a cursor as a dict"""
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql, *args)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]


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

    def distinct_count(self, qs, field_name, order_by=None, limit=None, filter_res=None):
        if filter_res is None:
            filter_res = {}
        results = qs.filter(**{field_name + "__isnull": False}, **filter_res).values(field_name).annotate(
            count=Count(field_name))
        if order_by:
            results = results.order_by('count') if order_by == 'ASC' else results.order_by('-count')
        else:
            results = results.order_by(field_name)
        if limit:
            results = results[:int(limit)]
        data = {}
        for r in results:
            data[str(r[field_name])] = r['count']
        return data

    def distinct_sum(self, qs, field_name, target, order_by=None, limit=None, filter_res=None):
        if filter_res is None:
            filter_res = {}
        results = qs.filter(**{field_name + "__isnull": False}, **filter_res).values(field_name).annotate(
            sum=Sum(target))
        if order_by:
            results = results.order_by('sum') if order_by == 'ASC' else results.order_by('-sum')
        else:
            results = results.order_by(field_name)
        if limit:
            results = results[:int(limit)]
        data = {}
        for r in results:
            data[str(r[field_name])] = r['sum']
        return data

    def distinct_avg(self, qs, field_name, target, order_by=None, limit=None, filter_res=None):
        if filter_res is None:
            filter_res = {}
        results = qs.filter(**{field_name+"__isnull": False}, **filter_res).values(field_name).annotate(avg=Avg(target))
        if order_by:
            results = results.order_by('avg') if order_by == 'ASC' else results.order_by('-avg')
        else:
            results = results.order_by(field_name)
        if limit:
            results = results[:int(limit)]
        data = {}
        for r in results:
            if not r['avg']:
                data[str(r[field_name])] = 0
            else:
                data[str(r[field_name])] = r['avg']
        return data

    def aggregate(self, qs, aggregate_conf, header_conf):
        res = self.date_to_str()
        special = ['distinct_count', 'distinct_sum', 'distinct_avg']
        result = {}
        data = []
        count_index = 0
        for conf in aggregate_conf['aggregate']:
            func = conf['func']
            field = conf['field']
            output = conf.get('output', field)
            r_data = {}
            if func in special:
                if func == 'distinct_count':
                    r_data = self.distinct_count(qs, field, conf.get('order_by'), conf.get('limit'), res)
                    for k in conf.get('keys', []):
                        r_data[str(k)] = r_data.get(str(k), 0)
                    result[output] = r_data
                elif func == 'distinct_sum':
                    r_data = self.distinct_sum(qs, field, conf['target'], conf.get('order_by'), conf.get('limit'), res)
                    for k in conf.get('keys', []):
                        r_data[str(k)] = r_data.get(str(k), 0)
                    result[output] = r_data
                elif func == 'distinct_avg':
                    r_data = self.distinct_avg(qs, field, conf['target'], conf.get('order_by'), conf.get('limit'), res)
                    for k in conf.get('keys', []):
                        r_data[str(k)] = r_data.get(str(k), 0)
                    result[output] = r_data
            else:
                result[output] = qs.aggregate(**{field: self.aggregate_func(func)(field)})[field]
            for k, v in r_data.items():
                item = {}
                if count_index == 0:
                    if header_conf[count_index + 1].get('percent'):
                        value = v * int(header_conf[count_index + 1].get('percent'))
                    elif header_conf[count_index + 1].get('eval'):
                        val = header_conf[count_index + 1].get('eval').format(v)
                        value = eval(val)
                    else:
                        value = v
                    if header_conf[count_index + 1].get('round'):
                        value = round(value, int(header_conf[count_index + 1].get('round')))
                    item[header_conf[count_index]['key']] = k
                    item[header_conf[count_index + 1]['key']] = value
                    data.append(item)
                else:
                    for d in data:
                        if d.get(header_conf[count_index + 1]['key']) is None:
                            if header_conf[count_index + 1].get('percent'):
                                value = v * int(header_conf[count_index + 1].get('percent'))
                            elif header_conf[count_index + 1].get('eval'):
                                val = header_conf[count_index + 1].get('eval').format(v)
                                value = eval(val)
                            else:
                                value = v
                            if header_conf[count_index + 1].get('round'):
                                value = round(value, int(header_conf[count_index + 1].get('round')))
                            d[header_conf[count_index + 1]['key']] = value
                            break
            count_index += 1
        return result, data

    def header_clean_data(self, headers, data):
        result = []
        for d in data:
            r_data = {}
            for i in headers:
                r_data[i] = d[i]
            result.append(r_data)
        return result

    def date_to_str(self):
        res = {}
        for key, value in self.request.GET.items():
            res[key] = value
        return res

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, report_id=kwargs['report_id'])
        flat_conf = obj.flat_config
        if flat_conf is None:
            get_list_or_404(models.FlatConfig, biz_id=obj.biz_id, org_id=obj.org_id, sys_id=obj.sys_id)
        qs = models.FlatData.objects.filter(
            org_id=obj.org_id, sys_id=obj.sys_id, biz_id=obj.biz_id
        )
        arguments_conf = self.parse_json(obj.arguments)
        data_struct_conf = self.parse_json(obj.data_struct)
        charts_struct_conf = self.parse_json(obj.charts_struct)

        # 重写的部分
        result_dict = {}
        data = []
        if 'aggregate' in arguments_conf:
            aggregates, data = self.aggregate(qs, arguments_conf, data_struct_conf.get('header', {}))
            result_dict['aggreate'] = aggregates
        elif 'sql' in arguments_conf:
            params = []
            res = self.date_to_str()
            if arguments_conf.get('sql_params'):
                for param in arguments_conf.get('sql_params'):
                    params.append(res.get(param))
            data = dictfetchall(arguments_conf.get('sql'), params)
        charts_struct_conf['detail'] = obj.report_name
        result_dict['id'] = kwargs['report_id']
        result_dict['title'] = obj.report_name
        result_dict['data'] = data
        result_dict['header'] = data_struct_conf.get('header', {})
        result_dict['charts'] = charts_struct_conf

        return Response(result_dict)
