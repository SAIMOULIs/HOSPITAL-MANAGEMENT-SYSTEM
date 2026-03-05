from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.appointment_list,   name='appointment_list'),
    path('<int:pk>/',               views.appointment_detail, name='appointment_detail'),
    path('add/',                    views.appointment_add,    name='appointment_add'),
    path('<int:pk>/edit/',          views.appointment_edit,   name='appointment_edit'),
    path('<int:pk>/delete/',        views.appointment_delete, name='appointment_delete'),
    path('<int:pk>/record/',        views.add_medical_record, name='add_medical_record'),
]
