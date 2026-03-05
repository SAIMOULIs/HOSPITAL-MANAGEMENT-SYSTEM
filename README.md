# 🏥 MediCare — Hospital Management System
> Built with Django + REST API + HTML/CSS | Fresher Interview Project

---

## 📋 Features

| Module | Features |
|--------|----------|
| 🔐 Auth | Login/Logout, Admin panel |
| 👥 Patients | Add, Edit, Delete, Search, View history |
| 👨‍⚕️ Doctors | Add, Edit, Delete, Departments |
| 📅 Appointments | Book, Update status, Filter by status |
| 📄 Medical Records | Diagnosis, Prescription, Fee |
| 🌐 REST API | Full CRUD for all modules via DRF |

---

## ⚡ Quick Start (5 minutes)

### Step 1 — Install Python 3.10+
Download from https://python.org

### Step 2 — Install dependencies
```bash
pip install Django djangorestframework Pillow
```
> For MySQL support also run: `pip install mysqlclient`

### Step 3 — Setup database & sample data
```bash
python manage.py migrate
python setup.py
```

### Step 4 — Run the server
```bash
python manage.py runserver
```

### Step 5 — Open browser
- 🏠 **Home:**    http://127.0.0.1:8000/
- 🔑 **Login:**   admin / admin123
- ⚙️  **Admin:**  http://127.0.0.1:8000/admin/
- 🌐 **API:**     http://127.0.0.1:8000/api/

---

## 🗄️ Switch to MySQL (Optional)

1. Create database in MySQL:
```sql
CREATE DATABASE hospital_db CHARACTER SET utf8mb4;
```

2. Edit `hospital_management/settings.py`, uncomment the MySQL section and fill in your credentials.

3. Run: `python manage.py migrate`

---

## 🌐 REST API Endpoints

| Endpoint | Methods |
|----------|---------|
| `/api/patients/` | GET, POST |
| `/api/patients/{id}/` | GET, PUT, PATCH, DELETE |
| `/api/doctors/` | GET, POST |
| `/api/doctors/{id}/` | GET, PUT, PATCH, DELETE |
| `/api/appointments/` | GET, POST |
| `/api/appointments/{id}/` | GET, PUT, PATCH, DELETE |
| `/api/departments/` | GET, POST |
| `/api/records/` | GET, POST |
| `/api/stats/` | GET (Dashboard stats) |

---

## 📁 Project Structure

```
hospital_management/
├── hospital_management/   # Django project settings
├── core/                  # Dashboard, Login, Base template
├── patients/              # Patient CRUD
├── doctors/               # Doctor + Department CRUD
├── appointments/          # Appointments + Medical Records
├── api/                   # REST API (DRF ViewSets)
├── setup.py               # One-click sample data setup
└── manage.py
```

---

## 🏆 Interview Talking Points

- **Django MTV architecture** (Models, Templates, Views)
- **REST API** using Django REST Framework (ViewSets + Routers)
- **Relational DB design** — ForeignKey, OneToOneField
- **Authentication** — Django built-in auth system
- **Role-based access** — @login_required decorator
- **ORM queries** — filter, select_related, annotate
- **MySQL ready** — configurable in settings.py

---

*Made with ❤️ for interview preparation*
