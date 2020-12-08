import json

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class FlatDataSerializer(ModelSerializer):

    class Meta:
        model = models.FlatData
        fields = (
            'id',
            'sys_id',
            'org_id',
            'biz_id',
            'field_01',
            'field_02',
            'field_03',
            'field_04',
            'field_05',
            'field_06',
            'field_07',
            'field_08',
            'field_09',
            'field_10',
            'field_11',
            'field_12',
            'field_13',
            'field_14',
            'field_15',
            'field_16',
            'field_17',
            'field_18',
            'field_19',
            'field_20',
            'field_21',
            'field_22',
            'field_23',
            'field_24',
            'field_25',
            'field_26',
            'field_27',
            'field_28',
            'field_29',
            'field_30',
            'date_01',
            'date_02',
            'date_03',
            'date_04',
            'date_05',
            'date_06',
            'date_07',
            'date_08',
            'date_09',
            'date_10',
            'datetime_01',
            'datetime_02',
            'datetime_03',
            'datetime_04',
            'datetime_05',
            'datetime_06',
            'datetime_07',
            'datetime_08',
            'datetime_09',
            'datetime_10',
            'int_01',
            'int_02',
            'int_03',
            'int_04',
            'int_05',
            'int_06',
            'int_07',
            'int_08',
            'int_09',
            'int_10',
            'float_01',
            'float_02',
            'float_03',
            'float_04',
            'float_05',
            'float_06',
            'float_07',
            'float_08',
            'float_09',
            'float_10',
        )


class FlatTemplateSerializer(ModelSerializer):

    class Meta:
        model = models.FlatTemplate
        fields = (
            'id',
            'sys_id',
            'org_id',
            'biz_id',
            'template_id',
            'template_name',
            'create_time',
            'update_time',
            'field_01',
            'field_02',
            'field_03',
            'field_04',
            'field_05',
            'field_06',
            'field_07',
            'field_08',
            'field_09',
            'field_10',
            'field_11',
            'field_12',
            'field_13',
            'field_14',
            'field_15',
            'field_16',
            'field_17',
            'field_18',
            'field_19',
            'field_20',
            'field_21',
            'field_22',
            'field_23',
            'field_24',
            'field_25',
            'field_26',
            'field_27',
            'field_28',
            'field_29',
            'field_30',
        )


class FlatConfigSerializer(ModelSerializer):

    class Meta:
        model = models.FlatConfig
        fields = (
            'id',
            'sys_id',
            'org_id',
            'biz_id',
            'field_01',
            'field_02',
            'field_03',
            'field_04',
            'field_05',
            'field_06',
            'field_07',
            'field_08',
            'field_09',
            'field_10',
            'field_11',
            'field_12',
            'field_13',
            'field_14',
            'field_15',
            'field_16',
            'field_17',
            'field_18',
            'field_19',
            'field_20',
            'field_21',
            'field_22',
            'field_23',
            'field_24',
            'field_25',
            'field_26',
            'field_27',
            'field_28',
            'field_29',
            'field_30',
            'int_01',
            'int_02',
            'int_03',
            'int_04',
            'int_05',
            'int_06',
            'int_07',
            'int_08',
            'int_09',
            'int_10',
            'float_01',
            'float_02',
            'float_03',
            'float_04',
            'float_05',
            'float_06',
            'float_07',
            'float_08',
            'float_09',
            'float_10',
        )


class FlatDataReportConfSerializer(ModelSerializer):
    filters = serializers.SerializerMethodField()

    class Meta:
        model = models.FlatDataReportConf
        fields = (
            'id',
            'sys_id',
            'org_id',
            'biz_id',
            'report_id',
            'report_name',
            'report_remark',
            'flat_config',
            'arguments',
            'data_struct',
            'charts_struct',
            'filters',
        )

    def get_filters(self, obj):
        ff = json.loads(obj.arguments).get('filter')
        if not ff:
            return []
        if isinstance(ff, list):
            fs = []
            for f in ff:
                if isinstance(f['option'], str):
                    item = {}
                    item[f['option']] = models.FlatData.objects.filter(biz_id=obj.biz_id).distinct(f['option']).values_list(f['option'], flat=True)
                    fs.append(item)
                elif isinstance(f['option'], list):
                    fs.append({f['key']: f['option']})
            return fs

