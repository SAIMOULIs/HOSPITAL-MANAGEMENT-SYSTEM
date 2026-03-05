from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient
from .forms import PatientForm


@login_required
def patient_list(request):
    q = request.GET.get('q', '')
    patients = Patient.objects.filter(first_name__icontains=q) | Patient.objects.filter(last_name__icontains=q) if q else Patient.objects.all().order_by('-created_at')
    return render(request, 'patients/list.html', {'patients': patients, 'q': q})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    appointments = patient.appointments.select_related('doctor').order_by('-appointment_date')
    return render(request, 'patients/detail.html', {'patient': patient, 'appointments': appointments})


@login_required
def patient_add(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Patient added successfully!')
        return redirect('patient_list')
    return render(request, 'patients/form.html', {'form': form, 'title': 'Add Patient'})


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        messages.success(request, 'Patient updated successfully!')
        return redirect('patient_detail', pk=pk)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Edit Patient'})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted.')
        return redirect('patient_list')
    return render(request, 'patients/confirm_delete.html', {'patient': patient})
