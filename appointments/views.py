from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment, MedicalRecord
from .forms import AppointmentForm, MedicalRecordForm


@login_required
def appointment_list(request):
    status = request.GET.get('status', '')
    appointments = Appointment.objects.select_related('patient', 'doctor').order_by('-appointment_date', '-appointment_time')
    if status:
        appointments = appointments.filter(status=status)
    return render(request, 'appointments/list.html', {'appointments': appointments, 'status': status})


@login_required
def appointment_detail(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    record = MedicalRecord.objects.filter(appointment=appt).first()
    return render(request, 'appointments/detail.html', {'appt': appt, 'record': record})


@login_required
def appointment_add(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Appointment booked successfully!')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Book Appointment'})


@login_required
def appointment_edit(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appt)
    if form.is_valid():
        form.save()
        messages.success(request, 'Appointment updated!')
        return redirect('appointment_detail', pk=pk)
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Edit Appointment'})


@login_required
def appointment_delete(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appt.delete()
        messages.success(request, 'Appointment deleted.')
        return redirect('appointment_list')
    return render(request, 'appointments/confirm_delete.html', {'appt': appt})


@login_required
def add_medical_record(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    existing = MedicalRecord.objects.filter(appointment=appt).first()
    form = MedicalRecordForm(request.POST or None, instance=existing)
    if form.is_valid():
        record = form.save(commit=False)
        record.appointment = appt
        record.save()
        appt.status = 'completed'
        appt.save()
        messages.success(request, 'Medical record saved!')
        return redirect('appointment_detail', pk=pk)
    return render(request, 'appointments/record_form.html', {'form': form, 'appt': appt})
