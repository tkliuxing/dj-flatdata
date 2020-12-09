import django_filters
from . import models


class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


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

    field_01_not = django_filters.CharFilter(field_name='field_01', exclude=True)
    field_02_not = django_filters.CharFilter(field_name='field_02', exclude=True)
    field_03_not = django_filters.CharFilter(field_name='field_03', exclude=True)
    field_04_not = django_filters.CharFilter(field_name='field_04', exclude=True)
    field_05_not = django_filters.CharFilter(field_name='field_05', exclude=True)
    field_06_not = django_filters.CharFilter(field_name='field_06', exclude=True)
    field_07_not = django_filters.CharFilter(field_name='field_07', exclude=True)
    field_08_not = django_filters.CharFilter(field_name='field_08', exclude=True)
    field_09_not = django_filters.CharFilter(field_name='field_09', exclude=True)
    field_10_not = django_filters.CharFilter(field_name='field_10', exclude=True)
    field_11_not = django_filters.CharFilter(field_name='field_11', exclude=True)
    field_12_not = django_filters.CharFilter(field_name='field_12', exclude=True)
    field_13_not = django_filters.CharFilter(field_name='field_13', exclude=True)
    field_14_not = django_filters.CharFilter(field_name='field_14', exclude=True)
    field_15_not = django_filters.CharFilter(field_name='field_15', exclude=True)
    field_16_not = django_filters.CharFilter(field_name='field_16', exclude=True)
    field_17_not = django_filters.CharFilter(field_name='field_17', exclude=True)
    field_18_not = django_filters.CharFilter(field_name='field_18', exclude=True)
    field_19_not = django_filters.CharFilter(field_name='field_19', exclude=True)
    field_20_not = django_filters.CharFilter(field_name='field_20', exclude=True)
    field_21_not = django_filters.CharFilter(field_name='field_21', exclude=True)
    field_22_not = django_filters.CharFilter(field_name='field_22', exclude=True)
    field_23_not = django_filters.CharFilter(field_name='field_23', exclude=True)
    field_24_not = django_filters.CharFilter(field_name='field_24', exclude=True)
    field_25_not = django_filters.CharFilter(field_name='field_25', exclude=True)
    field_26_not = django_filters.CharFilter(field_name='field_26', exclude=True)
    field_27_not = django_filters.CharFilter(field_name='field_27', exclude=True)
    field_28_not = django_filters.CharFilter(field_name='field_28', exclude=True)
    field_29_not = django_filters.CharFilter(field_name='field_29', exclude=True)
    field_30_not = django_filters.CharFilter(field_name='field_30', exclude=True)

    field_01_in = CharInFilter(field_name='field_01', lookup_expr='in')
    field_02_in = CharInFilter(field_name='field_02', lookup_expr='in')
    field_03_in = CharInFilter(field_name='field_03', lookup_expr='in')
    field_04_in = CharInFilter(field_name='field_04', lookup_expr='in')
    field_05_in = CharInFilter(field_name='field_05', lookup_expr='in')
    field_06_in = CharInFilter(field_name='field_06', lookup_expr='in')
    field_07_in = CharInFilter(field_name='field_07', lookup_expr='in')
    field_08_in = CharInFilter(field_name='field_08', lookup_expr='in')
    field_09_in = CharInFilter(field_name='field_09', lookup_expr='in')
    field_10_in = CharInFilter(field_name='field_10', lookup_expr='in')
    field_11_in = CharInFilter(field_name='field_11', lookup_expr='in')
    field_12_in = CharInFilter(field_name='field_12', lookup_expr='in')
    field_13_in = CharInFilter(field_name='field_13', lookup_expr='in')
    field_14_in = CharInFilter(field_name='field_14', lookup_expr='in')
    field_15_in = CharInFilter(field_name='field_15', lookup_expr='in')
    field_16_in = CharInFilter(field_name='field_16', lookup_expr='in')
    field_17_in = CharInFilter(field_name='field_17', lookup_expr='in')
    field_18_in = CharInFilter(field_name='field_18', lookup_expr='in')
    field_19_in = CharInFilter(field_name='field_19', lookup_expr='in')
    field_20_in = CharInFilter(field_name='field_20', lookup_expr='in')
    field_21_in = CharInFilter(field_name='field_21', lookup_expr='in')
    field_22_in = CharInFilter(field_name='field_22', lookup_expr='in')
    field_23_in = CharInFilter(field_name='field_23', lookup_expr='in')
    field_24_in = CharInFilter(field_name='field_24', lookup_expr='in')
    field_25_in = CharInFilter(field_name='field_25', lookup_expr='in')
    field_26_in = CharInFilter(field_name='field_26', lookup_expr='in')
    field_27_in = CharInFilter(field_name='field_27', lookup_expr='in')
    field_28_in = CharInFilter(field_name='field_28', lookup_expr='in')
    field_29_in = CharInFilter(field_name='field_29', lookup_expr='in')
    field_30_in = CharInFilter(field_name='field_30', lookup_expr='in')

    date_01_year = django_filters.NumberFilter(field_name='date_01', lookup_expr='year')
    date_02_year = django_filters.NumberFilter(field_name='date_02', lookup_expr='year')
    date_03_year = django_filters.NumberFilter(field_name='date_03', lookup_expr='year')
    date_04_year = django_filters.NumberFilter(field_name='date_04', lookup_expr='year')
    date_05_year = django_filters.NumberFilter(field_name='date_05', lookup_expr='year')
    date_06_year = django_filters.NumberFilter(field_name='date_06', lookup_expr='year')
    date_07_year = django_filters.NumberFilter(field_name='date_07', lookup_expr='year')
    date_08_year = django_filters.NumberFilter(field_name='date_08', lookup_expr='year')
    date_09_year = django_filters.NumberFilter(field_name='date_09', lookup_expr='year')
    date_10_year = django_filters.NumberFilter(field_name='date_10', lookup_expr='year')

    date_01_month = django_filters.NumberFilter(field_name='date_01', lookup_expr='month')
    date_02_month = django_filters.NumberFilter(field_name='date_02', lookup_expr='month')
    date_03_month = django_filters.NumberFilter(field_name='date_03', lookup_expr='month')
    date_04_month = django_filters.NumberFilter(field_name='date_04', lookup_expr='month')
    date_05_month = django_filters.NumberFilter(field_name='date_05', lookup_expr='month')
    date_06_month = django_filters.NumberFilter(field_name='date_06', lookup_expr='month')
    date_07_month = django_filters.NumberFilter(field_name='date_07', lookup_expr='month')
    date_08_month = django_filters.NumberFilter(field_name='date_08', lookup_expr='month')
    date_09_month = django_filters.NumberFilter(field_name='date_09', lookup_expr='month')
    date_10_month = django_filters.NumberFilter(field_name='date_10', lookup_expr='month')

    date_01_day = django_filters.NumberFilter(field_name='date_01', lookup_expr='day')
    date_02_day = django_filters.NumberFilter(field_name='date_02', lookup_expr='day')
    date_03_day = django_filters.NumberFilter(field_name='date_03', lookup_expr='day')
    date_04_day = django_filters.NumberFilter(field_name='date_04', lookup_expr='day')
    date_05_day = django_filters.NumberFilter(field_name='date_05', lookup_expr='day')
    date_06_day = django_filters.NumberFilter(field_name='date_06', lookup_expr='day')
    date_07_day = django_filters.NumberFilter(field_name='date_07', lookup_expr='day')
    date_08_day = django_filters.NumberFilter(field_name='date_08', lookup_expr='day')
    date_09_day = django_filters.NumberFilter(field_name='date_09', lookup_expr='day')
    date_10_day = django_filters.NumberFilter(field_name='date_10', lookup_expr='day')

    datetime_01_year = django_filters.NumberFilter(field_name='datetime_01', lookup_expr='year')
    datetime_02_year = django_filters.NumberFilter(field_name='datetime_02', lookup_expr='year')
    datetime_03_year = django_filters.NumberFilter(field_name='datetime_03', lookup_expr='year')
    datetime_04_year = django_filters.NumberFilter(field_name='datetime_04', lookup_expr='year')
    datetime_05_year = django_filters.NumberFilter(field_name='datetime_05', lookup_expr='year')
    datetime_06_year = django_filters.NumberFilter(field_name='datetime_06', lookup_expr='year')
    datetime_07_year = django_filters.NumberFilter(field_name='datetime_07', lookup_expr='year')
    datetime_08_year = django_filters.NumberFilter(field_name='datetime_08', lookup_expr='year')
    datetime_09_year = django_filters.NumberFilter(field_name='datetime_09', lookup_expr='year')
    datetime_10_year = django_filters.NumberFilter(field_name='datetime_10', lookup_expr='year')

    datetime_01_month = django_filters.NumberFilter(field_name='datetime_01', lookup_expr='month')
    datetime_02_month = django_filters.NumberFilter(field_name='datetime_02', lookup_expr='month')
    datetime_03_month = django_filters.NumberFilter(field_name='datetime_03', lookup_expr='month')
    datetime_04_month = django_filters.NumberFilter(field_name='datetime_04', lookup_expr='month')
    datetime_05_month = django_filters.NumberFilter(field_name='datetime_05', lookup_expr='month')
    datetime_06_month = django_filters.NumberFilter(field_name='datetime_06', lookup_expr='month')
    datetime_07_month = django_filters.NumberFilter(field_name='datetime_07', lookup_expr='month')
    datetime_08_month = django_filters.NumberFilter(field_name='datetime_08', lookup_expr='month')
    datetime_09_month = django_filters.NumberFilter(field_name='datetime_09', lookup_expr='month')
    datetime_10_month = django_filters.NumberFilter(field_name='datetime_10', lookup_expr='month')

    datetime_01_day = django_filters.NumberFilter(field_name='datetime_01', lookup_expr='day')
    datetime_02_day = django_filters.NumberFilter(field_name='datetime_02', lookup_expr='day')
    datetime_03_day = django_filters.NumberFilter(field_name='datetime_03', lookup_expr='day')
    datetime_04_day = django_filters.NumberFilter(field_name='datetime_04', lookup_expr='day')
    datetime_05_day = django_filters.NumberFilter(field_name='datetime_05', lookup_expr='day')
    datetime_06_day = django_filters.NumberFilter(field_name='datetime_06', lookup_expr='day')
    datetime_07_day = django_filters.NumberFilter(field_name='datetime_07', lookup_expr='day')
    datetime_08_day = django_filters.NumberFilter(field_name='datetime_08', lookup_expr='day')
    datetime_09_day = django_filters.NumberFilter(field_name='datetime_09', lookup_expr='day')
    datetime_10_day = django_filters.NumberFilter(field_name='datetime_10', lookup_expr='day')

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
