from django import forms
from .models import Appointment, MedicalRecord

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
            'notes':  forms.Textarea(attrs={'rows': 3}),
        }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'prescription', 'fee']
        widgets = {
            'diagnosis':    forms.Textarea(attrs={'rows': 4}),
            'prescription': forms.Textarea(attrs={'rows': 4}),
        }
