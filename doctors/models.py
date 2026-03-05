from django.db import models

class Department(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    department   = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    specialization = models.CharField(max_length=200)
    phone        = models.CharField(max_length=15)
    email        = models.EmailField()
    experience   = models.PositiveIntegerField(help_text="Years of experience")
    available    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"
