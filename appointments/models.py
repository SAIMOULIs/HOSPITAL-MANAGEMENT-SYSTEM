from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient         = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor          = models.ForeignKey(Doctor,  on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reason          = models.TextField()
    notes           = models.TextField(blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} -> {self.doctor} on {self.appointment_date}"

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']


class MedicalRecord(models.Model):
    appointment  = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='record')
    diagnosis    = models.TextField()
    prescription = models.TextField()
    fee          = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.appointment}"
