#!/usr/bin/env python
"""
Setup script — creates admin user and loads sample data.
Run: python setup.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User
from doctors.models import Department, Doctor
from patients.models import Patient
from appointments.models import Appointment
from datetime import date, time

print("🏥 Setting up MediCare Hospital Management System...")

# Admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@hospital.com', 'admin123')
    print("✅ Admin user created: admin / admin123")
else:
    print("ℹ️  Admin user already exists")

# Departments
depts_data = [
    ('Cardiology',    'Heart and cardiovascular diseases'),
    ('Neurology',     'Brain and nervous system disorders'),
    ('Orthopedics',   'Bone, joint, and muscle treatment'),
    ('Pediatrics',    'Medical care for children'),
    ('General Medicine', 'General health and primary care'),
    ('Dermatology',   'Skin, hair and nail disorders'),
]
depts = {}
for name, desc in depts_data:
    d, _ = Department.objects.get_or_create(name=name, defaults={'description': desc})
    depts[name] = d
print(f"✅ {len(depts)} departments created")

# Doctors
doctors_data = [
    ('Rajesh',  'Kumar',   'Cardiology',      'Cardiologist',        '9876543210', 'rajesh@hospital.com', 10),
    ('Priya',   'Sharma',  'Neurology',       'Neurologist',         '9876543211', 'priya@hospital.com',  8),
    ('Amit',    'Singh',   'Orthopedics',     'Orthopedic Surgeon',  '9876543212', 'amit@hospital.com',   12),
    ('Sunita',  'Patel',   'Pediatrics',      'Pediatrician',        '9876543213', 'sunita@hospital.com', 6),
    ('Ravi',    'Verma',   'General Medicine','General Physician',   '9876543214', 'ravi@hospital.com',   5),
]
doc_objs = []
for fn, ln, dept, spec, ph, em, exp in doctors_data:
    d, _ = Doctor.objects.get_or_create(
        first_name=fn, last_name=ln,
        defaults={'department': depts[dept], 'specialization': spec,
                  'phone': ph, 'email': em, 'experience': exp}
    )
    doc_objs.append(d)
print(f"✅ {len(doc_objs)} doctors created")

# Patients
patients_data = [
    ('Arjun',   'Mehta',   date(1990,5,15), 'M', 'O+',  '9000000001', 'arjun@gmail.com',   'Mumbai, Maharashtra'),
    ('Kavya',   'Reddy',   date(1985,3,22), 'F', 'B+',  '9000000002', 'kavya@gmail.com',   'Hyderabad, Telangana'),
    ('Sanjay',  'Gupta',   date(1978,11,8), 'M', 'A+',  '9000000003', 'sanjay@gmail.com',  'Delhi'),
    ('Meera',   'Nair',    date(1995,7,30), 'F', 'AB+', '9000000004', 'meera@gmail.com',   'Chennai, Tamil Nadu'),
    ('Vikram',  'Joshi',   date(2001,1,12), 'M', 'O-',  '9000000005', 'vikram@gmail.com',  'Pune, Maharashtra'),
]
pat_objs = []
for fn, ln, dob, gen, bg, ph, em, addr in patients_data:
    p, _ = Patient.objects.get_or_create(
        first_name=fn, last_name=ln,
        defaults={'date_of_birth': dob, 'gender': gen, 'blood_group': bg,
                  'phone': ph, 'email': em, 'address': addr}
    )
    pat_objs.append(p)
print(f"✅ {len(pat_objs)} patients created")

# Appointments
if Appointment.objects.count() == 0:
    appts = [
        (pat_objs[0], doc_objs[0], date.today(), time(10,0), 'confirmed', 'Chest pain and shortness of breath'),
        (pat_objs[1], doc_objs[1], date.today(), time(11,30),'pending',   'Severe headache for 3 days'),
        (pat_objs[2], doc_objs[2], date.today(), time(14,0), 'pending',   'Knee joint pain'),
        (pat_objs[3], doc_objs[3], date(2025,1,10), time(9,0),'completed','Fever and cold'),
        (pat_objs[4], doc_objs[4], date(2025,1,12), time(16,0),'completed','General checkup'),
    ]
    for p, d, dt, t, st, reason in appts:
        Appointment.objects.create(patient=p, doctor=d, appointment_date=dt,
                                   appointment_time=t, status=st, reason=reason)
    print(f"✅ {len(appts)} sample appointments created")

print("\n🎉 Setup complete!")
print("━" * 40)
print("▶  Run:  python manage.py runserver")
print("▶  Open: http://127.0.0.1:8000/")
print("▶  Login: admin / admin123")
print("▶  API:  http://127.0.0.1:8000/api/")
print("━" * 40)
