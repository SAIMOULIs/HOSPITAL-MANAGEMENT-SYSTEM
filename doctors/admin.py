from django.contrib import admin
from .models import Doctor, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'department', 'specialization', 'experience', 'available']
    list_filter = ['department', 'available']
    search_fields = ['first_name', 'last_name', 'specialization']
