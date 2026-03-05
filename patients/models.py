from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    BLOOD_CHOICES = [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),
                     ('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')]

    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender        = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group   = models.CharField(max_length=3, choices=BLOOD_CHOICES)
    phone         = models.CharField(max_length=15)
    email         = models.EmailField(blank=True)
    address       = models.TextField()
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
