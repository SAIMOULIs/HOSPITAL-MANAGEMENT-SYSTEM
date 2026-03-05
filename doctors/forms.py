from django import forms
from .models import Doctor, Department

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}
