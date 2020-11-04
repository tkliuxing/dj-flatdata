from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api


router = DefaultRouter()

router.register(r'flatdata', api.FlatDataViewSet)
router.register(r'flatconfig', api.FlatConfigViewSet)
router.register(r'flattemplate', api.FlatTemplateViewSet)
router.register(r'flatdatareportconf', api.FlatDataReportConfViewSet)
router.register(r'flatdatareportconfcopy', api.FlatDataReportConfCopyView)

urlpatterns = (
    path('api/v1/', include(router.urls)),
    path('api/v1/flatdatareport/<int:report_id>/', api.FlatDataReportView.as_view()),
)
