from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.doctor_list,     name='doctor_list'),
    path('<int:pk>/',           views.doctor_detail,   name='doctor_detail'),
    path('add/',                views.doctor_add,      name='doctor_add'),
    path('<int:pk>/edit/',      views.doctor_edit,     name='doctor_edit'),
    path('<int:pk>/delete/',    views.doctor_delete,   name='doctor_delete'),
    path('departments/',        views.department_list, name='department_list'),
    path('departments/add/',    views.department_add,  name='department_add'),
]
