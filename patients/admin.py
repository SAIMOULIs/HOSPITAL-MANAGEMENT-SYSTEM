from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'blood_group', 'phone', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone']
