from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('patients',     views.PatientViewSet)
router.register('departments',  views.DepartmentViewSet)
router.register('doctors',      views.DoctorViewSet)
router.register('appointments', views.AppointmentViewSet)
router.register('records',      views.MedicalRecordViewSet)

urlpatterns = [
    path('',       include(router.urls)),
    path('stats/', views.api_stats, name='api_stats'),
]
