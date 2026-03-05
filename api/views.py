from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from patients.models import Patient
from doctors.models import Doctor, Department
from appointments.models import Appointment, MedicalRecord
from .serializers import (PatientSerializer, DoctorSerializer, DepartmentSerializer,
                           AppointmentSerializer, MedicalRecordSerializer)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'phone']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.select_related('department').all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'specialization']


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related('patient', 'doctor').all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__first_name', 'doctor__first_name', 'status']


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


@api_view(['GET'])
def api_stats(request):
    from django.utils import timezone
    today = timezone.now().date()
    return Response({
        'total_patients':      Patient.objects.count(),
        'total_doctors':       Doctor.objects.count(),
        'total_appointments':  Appointment.objects.count(),
        'today_appointments':  Appointment.objects.filter(appointment_date=today).count(),
        'pending':             Appointment.objects.filter(status='pending').count(),
        'completed':           Appointment.objects.filter(status='completed').count(),
    })
