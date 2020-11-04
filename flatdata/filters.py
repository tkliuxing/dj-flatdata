import django_filters
from . import models

class FlatDataFilterSet(django_filters.FilterSet):
    field_01_null = django_filters.BooleanFilter(field_name='field_01', lookup_expr='isnull')
    field_02_null = django_filters.BooleanFilter(field_name='field_02', lookup_expr='isnull')
    field_03_null = django_filters.BooleanFilter(field_name='field_03', lookup_expr='isnull')
    field_04_null = django_filters.BooleanFilter(field_name='field_04', lookup_expr='isnull')
    field_05_null = django_filters.BooleanFilter(field_name='field_05', lookup_expr='isnull')
    field_06_null = django_filters.BooleanFilter(field_name='field_06', lookup_expr='isnull')
    field_07_null = django_filters.BooleanFilter(field_name='field_07', lookup_expr='isnull')
    field_08_null = django_filters.BooleanFilter(field_name='field_08', lookup_expr='isnull')
    field_09_null = django_filters.BooleanFilter(field_name='field_09', lookup_expr='isnull')
    field_10_null = django_filters.BooleanFilter(field_name='field_10', lookup_expr='isnull')
    field_11_null = django_filters.BooleanFilter(field_name='field_11', lookup_expr='isnull')
    field_12_null = django_filters.BooleanFilter(field_name='field_12', lookup_expr='isnull')
    field_13_null = django_filters.BooleanFilter(field_name='field_13', lookup_expr='isnull')
    field_14_null = django_filters.BooleanFilter(field_name='field_14', lookup_expr='isnull')
    field_15_null = django_filters.BooleanFilter(field_name='field_15', lookup_expr='isnull')
    field_16_null = django_filters.BooleanFilter(field_name='field_16', lookup_expr='isnull')
    field_17_null = django_filters.BooleanFilter(field_name='field_17', lookup_expr='isnull')
    field_18_null = django_filters.BooleanFilter(field_name='field_18', lookup_expr='isnull')
    field_19_null = django_filters.BooleanFilter(field_name='field_19', lookup_expr='isnull')
    field_20_null = django_filters.BooleanFilter(field_name='field_20', lookup_expr='isnull')
    field_21_null = django_filters.BooleanFilter(field_name='field_21', lookup_expr='isnull')
    field_22_null = django_filters.BooleanFilter(field_name='field_22', lookup_expr='isnull')
    field_23_null = django_filters.BooleanFilter(field_name='field_23', lookup_expr='isnull')
    field_24_null = django_filters.BooleanFilter(field_name='field_24', lookup_expr='isnull')
    field_25_null = django_filters.BooleanFilter(field_name='field_25', lookup_expr='isnull')
    field_26_null = django_filters.BooleanFilter(field_name='field_26', lookup_expr='isnull')
    field_27_null = django_filters.BooleanFilter(field_name='field_27', lookup_expr='isnull')
    field_28_null = django_filters.BooleanFilter(field_name='field_28', lookup_expr='isnull')
    field_29_null = django_filters.BooleanFilter(field_name='field_29', lookup_expr='isnull')
    field_30_null = django_filters.BooleanFilter(field_name='field_30', lookup_expr='isnull')

    int_01_range = django_filters.RangeFilter(field_name='int_01', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_02_range = django_filters.RangeFilter(field_name='int_02', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_03_range = django_filters.RangeFilter(field_name='int_03', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_04_range = django_filters.RangeFilter(field_name='int_04', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_05_range = django_filters.RangeFilter(field_name='int_05', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_06_range = django_filters.RangeFilter(field_name='int_06', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_07_range = django_filters.RangeFilter(field_name='int_07', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_08_range = django_filters.RangeFilter(field_name='int_08', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_09_range = django_filters.RangeFilter(field_name='int_09', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    int_10_range = django_filters.RangeFilter(field_name='int_10', help_text='int_xx_range_min=xx&int_xx_range_max=xx')
    float_01_range = django_filters.RangeFilter(field_name='float_01', help_text='')
    float_02_range = django_filters.RangeFilter(field_name='float_02', help_text='')
    float_03_range = django_filters.RangeFilter(field_name='float_03', help_text='')
    float_04_range = django_filters.RangeFilter(field_name='float_04', help_text='')
    float_05_range = django_filters.RangeFilter(field_name='float_05', help_text='')
    float_06_range = django_filters.RangeFilter(field_name='float_06', help_text='')
    float_07_range = django_filters.RangeFilter(field_name='float_07', help_text='')
    float_08_range = django_filters.RangeFilter(field_name='float_08', help_text='')
    float_09_range = django_filters.RangeFilter(field_name='float_09', help_text='')
    float_10_range = django_filters.RangeFilter(field_name='float_10', help_text='')

    class Meta:
        model = models.FlatData
        fields = (
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