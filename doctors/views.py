from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor, Department
from .forms import DoctorForm, DepartmentForm


@login_required
def doctor_list(request):
    q = request.GET.get('q', '')
    doctors = Doctor.objects.filter(first_name__icontains=q) | Doctor.objects.filter(specialization__icontains=q) if q else Doctor.objects.select_related('department').all()
    return render(request, 'doctors/list.html', {'doctors': doctors, 'q': q})


@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    appointments = doctor.appointments.select_related('patient').order_by('-appointment_date')[:10]
    return render(request, 'doctors/detail.html', {'doctor': doctor, 'appointments': appointments})


@login_required
def doctor_add(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Doctor added successfully!')
        return redirect('doctor_list')
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Add Doctor'})


@login_required
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Doctor updated!')
        return redirect('doctor_detail', pk=pk)
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Edit Doctor'})


@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted.')
        return redirect('doctor_list')
    return render(request, 'doctors/confirm_delete.html', {'doctor': doctor})


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'doctors/departments.html', {'departments': departments})


@login_required
def department_add(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Department added!')
        return redirect('department_list')
    return render(request, 'doctors/dept_form.html', {'form': form, 'title': 'Add Department'})
