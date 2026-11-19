# NasiyeClinic – Django Clinic Management System

## Project Overview

NasiyeClinic is a Clinic Management System developed using Django, Python, SQLite, Bootstrap 5, and Django Template Language (DTL).

The system helps manage doctors, patients, appointments, and clinic information through a simple and user-friendly interface.

## Technologies Used

- Python
- Django
- SQLite
- HTML and CSS
- Bootstrap 5
- Django Template Language (DTL)

## Main Features

- Home page with a three-image carousel
- Doctor management
- Patient registration and management
- Appointment scheduling
- Appointment list
- Contact page
- Dashboard with general statistics
- User login and logout
- Django Admin Panel

## Project Structure

The project contains the following Django applications:

- **core:** Home page, contact page, and registration.
- **doctors:** Doctor information and management.
- **patients:** Patient information and management.
- **appointments:** Appointment scheduling and management.
- **dashboard:** General clinic statistics.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/huda-saed/nasiyeclinic-django-project11.git
cd nasiyeclinic-django-project11
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

## Access the System

Open your browser and visit:

- **Home Page:** http://127.0.0.1:8000/
- **Login:** http://127.0.0.1:8000/login/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## User Authentication

The system supports user authentication through login and logout.

Important pages such as Dashboard, Patients, Schedule, and Appointments require users to log in.

## Admin Panel

The Django Admin Panel allows administrators to manage Doctor, Patient, and Appointment records.

## Database

The project uses SQLite. The database is created locally by running Django migrations.

## Developer

**Project Name:** NasiyeClinic  
**Project Type:** Clinic Management System  
**Framework:** Django  
**Database:** SQLite