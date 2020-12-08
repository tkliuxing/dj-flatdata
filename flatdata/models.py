from django.db import models
from django.utils import timezone


class FlatData(models.Model):
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    field_01 = models.CharField('Field 01', max_length=1023, null=True, blank=True, db_index=True)
    field_02 = models.CharField('Field 02', max_length=1023, null=True, blank=True, db_index=True)
    field_03 = models.CharField('Field 03', max_length=1023, null=True, blank=True, db_index=True)
    field_04 = models.CharField('Field 04', max_length=1023, null=True, blank=True, db_index=True)
    field_05 = models.CharField('Field 05', max_length=1023, null=True, blank=True, db_index=True)
    field_06 = models.CharField('Field 06', max_length=1023, null=True, blank=True, db_index=True)
    field_07 = models.CharField('Field 07', max_length=1023, null=True, blank=True, db_index=True)
    field_08 = models.CharField('Field 08', max_length=1023, null=True, blank=True, db_index=True)
    field_09 = models.CharField('Field 09', max_length=1023, null=True, blank=True, db_index=True)
    field_10 = models.CharField('Field 10', max_length=1023, null=True, blank=True, db_index=True)
    field_11 = models.CharField('Field 11', max_length=1023, null=True, blank=True, db_index=True)
    field_12 = models.CharField('Field 12', max_length=1023, null=True, blank=True, db_index=True)
    field_13 = models.CharField('Field 13', max_length=1023, null=True, blank=True, db_index=True)
    field_14 = models.CharField('Field 14', max_length=1023, null=True, blank=True, db_index=True)
    field_15 = models.CharField('Field 15', max_length=1023, null=True, blank=True, db_index=True)
    field_16 = models.CharField('Field 16', max_length=1023, null=True, blank=True, db_index=True)
    field_17 = models.CharField('Field 17', max_length=1023, null=True, blank=True, db_index=True)
    field_18 = models.CharField('Field 18', max_length=1023, null=True, blank=True, db_index=True)
    field_19 = models.CharField('Field 19', max_length=1023, null=True, blank=True, db_index=True)
    field_20 = models.CharField('Field 20', max_length=1023, null=True, blank=True, db_index=True)
    field_21 = models.CharField('Field 21', max_length=1023, null=True, blank=True, db_index=True)
    field_22 = models.CharField('Field 22', max_length=1023, null=True, blank=True, db_index=True)
    field_23 = models.CharField('Field 23', max_length=1023, null=True, blank=True, db_index=True)
    field_24 = models.CharField('Field 24', max_length=1023, null=True, blank=True, db_index=True)
    field_25 = models.CharField('Field 25', max_length=1023, null=True, blank=True, db_index=True)
    field_26 = models.CharField('Field 26', max_length=1023, null=True, blank=True, db_index=True)
    field_27 = models.CharField('Field 27', max_length=1023, null=True, blank=True, db_index=True)
    field_28 = models.CharField('Field 28', max_length=1023, null=True, blank=True, db_index=True)
    field_29 = models.CharField('Field 29', max_length=1023, null=True, blank=True, db_index=True)
    field_30 = models.CharField('Field 30', max_length=1023, null=True, blank=True, db_index=True)

    date_01 = models.DateField('Date 01', null=True, blank=True, db_index=True)
    date_02 = models.DateField('Date 02', null=True, blank=True, db_index=True)
    date_03 = models.DateField('Date 03', null=True, blank=True, db_index=True)
    date_04 = models.DateField('Date 04', null=True, blank=True, db_index=True)
    date_05 = models.DateField('Date 05', null=True, blank=True, db_index=True)
    date_06 = models.DateField('Date 06', null=True, blank=True, db_index=True)
    date_07 = models.DateField('Date 07', null=True, blank=True, db_index=True)
    date_08 = models.DateField('Date 08', null=True, blank=True, db_index=True)
    date_09 = models.DateField('Date 09', null=True, blank=True, db_index=True)
    date_10 = models.DateField('Date 10', null=True, blank=True, db_index=True)

    datetime_01 = models.DateTimeField('DateTime 01', null=True, blank=True, db_index=True)
    datetime_02 = models.DateTimeField('DateTime 02', null=True, blank=True, db_index=True)
    datetime_03 = models.DateTimeField('DateTime 03', null=True, blank=True, db_index=True)
    datetime_04 = models.DateTimeField('DateTime 04', null=True, blank=True, db_index=True)
    datetime_05 = models.DateTimeField('DateTime 05', null=True, blank=True, db_index=True)
    datetime_06 = models.DateTimeField('DateTime 06', null=True, blank=True, db_index=True)
    datetime_07 = models.DateTimeField('DateTime 07', null=True, blank=True, db_index=True)
    datetime_08 = models.DateTimeField('DateTime 08', null=True, blank=True, db_index=True)
    datetime_09 = models.DateTimeField('DateTime 09', null=True, blank=True, db_index=True)
    datetime_10 = models.DateTimeField('DateTime 10', null=True, blank=True, db_index=True)

    int_01 = models.BigIntegerField('Int 01', null=True, blank=True, db_index=True)
    int_02 = models.BigIntegerField('Int 02', null=True, blank=True, db_index=True)
    int_03 = models.BigIntegerField('Int 03', null=True, blank=True, db_index=True)
    int_04 = models.BigIntegerField('Int 04', null=True, blank=True, db_index=True)
    int_05 = models.BigIntegerField('Int 05', null=True, blank=True, db_index=True)
    int_06 = models.BigIntegerField('Int 06', null=True, blank=True, db_index=True)
    int_07 = models.BigIntegerField('Int 07', null=True, blank=True, db_index=True)
    int_08 = models.BigIntegerField('Int 08', null=True, blank=True, db_index=True)
    int_09 = models.BigIntegerField('Int 09', null=True, blank=True, db_index=True)
    int_10 = models.BigIntegerField('Int 10', null=True, blank=True, db_index=True)

    float_01 = models.FloatField('Float 01', null=True, blank=True, db_index=True)
    float_02 = models.FloatField('Float 02', null=True, blank=True, db_index=True)
    float_03 = models.FloatField('Float 03', null=True, blank=True, db_index=True)
    float_04 = models.FloatField('Float 04', null=True, blank=True, db_index=True)
    float_05 = models.FloatField('Float 05', null=True, blank=True, db_index=True)
    float_06 = models.FloatField('Float 06', null=True, blank=True, db_index=True)
    float_07 = models.FloatField('Float 07', null=True, blank=True, db_index=True)
    float_08 = models.FloatField('Float 08', null=True, blank=True, db_index=True)
    float_09 = models.FloatField('Float 09', null=True, blank=True, db_index=True)
    float_10 = models.FloatField('Float 10', null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = '数据表'
        verbose_name_plural = verbose_name


class FlatTemplate(models.Model):
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    template_id = models.IntegerField('模板ID', default=1, db_index=True, unique=True)
    template_name = models.CharField('模板名称', max_length=31, null=True, blank=True, help_text='模板名称')
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    field_01 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_02 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_03 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_04 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_05 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_06 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_07 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_08 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_09 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_10 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_11 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_12 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_13 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_14 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_15 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_16 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_17 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_18 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_19 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_20 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_21 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_22 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_23 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_24 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_25 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_26 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_27 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_28 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_29 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )
    field_30 = models.ForeignKey(
        'baseconfig.BaseConfigItem', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="+", verbose_name='模板字段', help_text='模板字段'
    )

    class Meta:
        verbose_name = '数据表模板'
        verbose_name_plural = verbose_name


class FlatConfig(models.Model):
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    field_01 = models.CharField('Field 01', max_length=1023, null=True, blank=True, db_index=True)
    field_02 = models.CharField('Field 02', max_length=1023, null=True, blank=True, db_index=True)
    field_03 = models.CharField('Field 03', max_length=1023, null=True, blank=True, db_index=True)
    field_04 = models.CharField('Field 04', max_length=1023, null=True, blank=True, db_index=True)
    field_05 = models.CharField('Field 05', max_length=1023, null=True, blank=True, db_index=True)
    field_06 = models.CharField('Field 06', max_length=1023, null=True, blank=True, db_index=True)
    field_07 = models.CharField('Field 07', max_length=1023, null=True, blank=True, db_index=True)
    field_08 = models.CharField('Field 08', max_length=1023, null=True, blank=True, db_index=True)
    field_09 = models.CharField('Field 09', max_length=1023, null=True, blank=True, db_index=True)
    field_10 = models.CharField('Field 10', max_length=1023, null=True, blank=True, db_index=True)
    field_11 = models.CharField('Field 11', max_length=1023, null=True, blank=True, db_index=True)
    field_12 = models.CharField('Field 12', max_length=1023, null=True, blank=True, db_index=True)
    field_13 = models.CharField('Field 13', max_length=1023, null=True, blank=True, db_index=True)
    field_14 = models.CharField('Field 14', max_length=1023, null=True, blank=True, db_index=True)
    field_15 = models.CharField('Field 15', max_length=1023, null=True, blank=True, db_index=True)
    field_16 = models.CharField('Field 16', max_length=1023, null=True, blank=True, db_index=True)
    field_17 = models.CharField('Field 17', max_length=1023, null=True, blank=True, db_index=True)
    field_18 = models.CharField('Field 18', max_length=1023, null=True, blank=True, db_index=True)
    field_19 = models.CharField('Field 19', max_length=1023, null=True, blank=True, db_index=True)
    field_20 = models.CharField('Field 20', max_length=1023, null=True, blank=True, db_index=True)
    field_21 = models.CharField('Field 21', max_length=1023, null=True, blank=True, db_index=True)
    field_22 = models.CharField('Field 22', max_length=1023, null=True, blank=True, db_index=True)
    field_23 = models.CharField('Field 23', max_length=1023, null=True, blank=True, db_index=True)
    field_24 = models.CharField('Field 24', max_length=1023, null=True, blank=True, db_index=True)
    field_25 = models.CharField('Field 25', max_length=1023, null=True, blank=True, db_index=True)
    field_26 = models.CharField('Field 26', max_length=1023, null=True, blank=True, db_index=True)
    field_27 = models.CharField('Field 27', max_length=1023, null=True, blank=True, db_index=True)
    field_28 = models.CharField('Field 28', max_length=1023, null=True, blank=True, db_index=True)
    field_29 = models.CharField('Field 29', max_length=1023, null=True, blank=True, db_index=True)
    field_30 = models.CharField('Field 30', max_length=1023, null=True, blank=True, db_index=True)
    int_01 = models.CharField('Int 01', max_length=1023, null=True, blank=True, db_index=True)
    int_02 = models.CharField('Int 02', max_length=1023, null=True, blank=True, db_index=True)
    int_03 = models.CharField('Int 03', max_length=1023, null=True, blank=True, db_index=True)
    int_04 = models.CharField('Int 04', max_length=1023, null=True, blank=True, db_index=True)
    int_05 = models.CharField('Int 05', max_length=1023, null=True, blank=True, db_index=True)
    int_06 = models.CharField('Int 06', max_length=1023, null=True, blank=True, db_index=True)
    int_07 = models.CharField('Int 07', max_length=1023, null=True, blank=True, db_index=True)
    int_08 = models.CharField('Int 08', max_length=1023, null=True, blank=True, db_index=True)
    int_09 = models.CharField('Int 09', max_length=1023, null=True, blank=True, db_index=True)
    int_10 = models.CharField('Int 10', max_length=1023, null=True, blank=True, db_index=True)
    float_01 = models.CharField('Float 01', max_length=1023, null=True, blank=True, db_index=True)
    float_02 = models.CharField('Float 02', max_length=1023, null=True, blank=True, db_index=True)
    float_03 = models.CharField('Float 03', max_length=1023, null=True, blank=True, db_index=True)
    float_04 = models.CharField('Float 04', max_length=1023, null=True, blank=True, db_index=True)
    float_05 = models.CharField('Float 05', max_length=1023, null=True, blank=True, db_index=True)
    float_06 = models.CharField('Float 06', max_length=1023, null=True, blank=True, db_index=True)
    float_07 = models.CharField('Float 07', max_length=1023, null=True, blank=True, db_index=True)
    float_08 = models.CharField('Float 08', max_length=1023, null=True, blank=True, db_index=True)
    float_09 = models.CharField('Float 09', max_length=1023, null=True, blank=True, db_index=True)
    float_10 = models.CharField('Float 10', max_length=1023, null=True, blank=True, db_index=True)
    field_type_01 = models.CharField('Field Type 01', max_length=15, null=True, blank=True, db_index=True)
    field_type_02 = models.CharField('Field Type 02', max_length=15, null=True, blank=True, db_index=True)
    field_type_03 = models.CharField('Field Type 03', max_length=15, null=True, blank=True, db_index=True)
    field_type_04 = models.CharField('Field Type 04', max_length=15, null=True, blank=True, db_index=True)
    field_type_05 = models.CharField('Field Type 05', max_length=15, null=True, blank=True, db_index=True)
    field_type_06 = models.CharField('Field Type 06', max_length=15, null=True, blank=True, db_index=True)
    field_type_07 = models.CharField('Field Type 07', max_length=15, null=True, blank=True, db_index=True)
    field_type_08 = models.CharField('Field Type 08', max_length=15, null=True, blank=True, db_index=True)
    field_type_09 = models.CharField('Field Type 09', max_length=15, null=True, blank=True, db_index=True)
    field_type_10 = models.CharField('Field Type 10', max_length=15, null=True, blank=True, db_index=True)
    field_type_11 = models.CharField('Field Type 11', max_length=15, null=True, blank=True, db_index=True)
    field_type_12 = models.CharField('Field Type 12', max_length=15, null=True, blank=True, db_index=True)
    field_type_13 = models.CharField('Field Type 13', max_length=15, null=True, blank=True, db_index=True)
    field_type_14 = models.CharField('Field Type 14', max_length=15, null=True, blank=True, db_index=True)
    field_type_15 = models.CharField('Field Type 15', max_length=15, null=True, blank=True, db_index=True)
    field_type_16 = models.CharField('Field Type 16', max_length=15, null=True, blank=True, db_index=True)
    field_type_17 = models.CharField('Field Type 17', max_length=15, null=True, blank=True, db_index=True)
    field_type_18 = models.CharField('Field Type 18', max_length=15, null=True, blank=True, db_index=True)
    field_type_19 = models.CharField('Field Type 19', max_length=15, null=True, blank=True, db_index=True)
    field_type_20 = models.CharField('Field Type 20', max_length=15, null=True, blank=True, db_index=True)
    field_type_21 = models.CharField('Field Type 21', max_length=15, null=True, blank=True, db_index=True)
    field_type_22 = models.CharField('Field Type 22', max_length=15, null=True, blank=True, db_index=True)
    field_type_23 = models.CharField('Field Type 23', max_length=15, null=True, blank=True, db_index=True)
    field_type_24 = models.CharField('Field Type 24', max_length=15, null=True, blank=True, db_index=True)
    field_type_25 = models.CharField('Field Type 25', max_length=15, null=True, blank=True, db_index=True)
    field_type_26 = models.CharField('Field Type 26', max_length=15, null=True, blank=True, db_index=True)
    field_type_27 = models.CharField('Field Type 27', max_length=15, null=True, blank=True, db_index=True)
    field_type_28 = models.CharField('Field Type 28', max_length=15, null=True, blank=True, db_index=True)
    field_type_29 = models.CharField('Field Type 29', max_length=15, null=True, blank=True, db_index=True)
    field_type_30 = models.CharField('Field Type 30', max_length=15, null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = '数据定义表'
        verbose_name_plural = verbose_name


class FlatDataReportConf(models.Model):
    sys_id = models.IntegerField('系统ID', default=1, db_index=True)
    org_id = models.IntegerField('组织ID', default=1, db_index=True)
    biz_id = models.IntegerField('业务ID', default=1, db_index=True)
    report_id = models.IntegerField('报表ID', default=1, db_index=True, unique=True)
    report_name = models.CharField('报表名称', max_length=31, null=True, blank=True, db_index=True, help_text='报表名称')
    report_remark = models.TextField('报表说明', null=True, blank=True, help_text='报表说明')
    flat_config = models.ForeignKey('FlatConfig', on_delete=models.SET_NULL, null=True, blank=True)
    arguments = models.TextField('参数定义', null=True, blank=True, help_text='参数定义')
    data_struct = models.TextField('数据定义', null=True, blank=True, help_text='数据定义')
    charts_struct = models.TextField('图表定义', null=True, blank=True, help_text='图表定义')

    class Meta:
        verbose_name = '数据报表'
        verbose_name_plural = verbose_name
