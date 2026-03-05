from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from patients.models import Patient
from doctors.models import Doctor, Department
from appointments.models import Appointment, MedicalRecord
from django.utils import timezone


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    today = timezone.now().date()
    context = {
        'total_patients':     Patient.objects.count(),
        'total_doctors':      Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'today_appointments': Appointment.objects.filter(appointment_date=today).count(),
        'pending':            Appointment.objects.filter(status='pending').count(),
        'completed':          Appointment.objects.filter(status='completed').count(),
        'departments':        Department.objects.count(),
        'recent_appointments': Appointment.objects.select_related('patient','doctor').order_by('-created_at')[:5],
    }
    return render(request, 'core/dashboard.html', context)
