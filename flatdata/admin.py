from django.contrib import admin
from . import models


@admin.register(models.FlatData)
class FlatDataAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', ]


@admin.register(models.FlatConfig)
class FlatConfigAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', ]


@admin.register(models.FlatTemplate)
class FlatTemplateAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'template_id', 'template_name']
    list_display_links = ['pk', 'sys_id', 'org_id', 'biz_id', 'template_id', 'template_name']


@admin.register(models.FlatDataReportConf)
class FlatDataReportConfAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sys_id', 'org_id', 'biz_id', 'report_id', 'report_name']
    list_display_links = ['pk', 'sys_id', 'org_id', 'biz_id', 'report_id', 'report_name']
