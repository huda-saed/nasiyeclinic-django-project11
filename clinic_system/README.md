# NasiyeClinic - Django Clinic Management System

Project ka waxa uu daboolayaa dhammaan shuruudaha hawlgalka:
Django, SQLite, Bootstrap 5, iyo Django Template Language (DTL).

## Sida loo Shaqaysiiyo (Setup)

1. Samee virtual environment (optional laakiin la talinayaa):
   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Rakib package-yada loo baahan yahay:
   ```
   pip install -r requirements.txt
   ```

3. Migrations-ka horeba way ku jiraan project-ka (kuma baahnid `makemigrations`). Kaliya samee migrate si loo abuuro database-ka:
   ```
   python manage.py migrate
   ```

4. Samee superuser si aad admin page uga geli karto:
   ```
   python manage.py createsuperuser
   ```

5. Bilaw server-ka:
   ```
   python manage.py runserver
   ```

6. Fur browser-kaaga oo tag: `http://127.0.0.1:8000/`
   Admin page: `http://127.0.0.1:8000/admin/`

## Qaab-dhismeedka Project-ka (Apps)

- **core** — Home page (carousel 3 sawir), Contact page, Register
- **doctors** — Doctor model + Doctors page
- **patients** — Patient model (ID, Full Name, Gender, Date of Birth, Phone Number, Email) + Patients page
- **appointments** — Appointment model + Schedule page (Fullname, Appoint name, Time in, Time out, Date) + Appointment list page
- **dashboard** — Dashboard page oo tuso tirakoobka guud

## Boggagga (6 Pages)

1. Base page (`templates/base.html`) — dhammaan boggagga way ka dhaxlaan (extends)
2. Home page — carousel 3 sawir + adeegyada + dhakhaatiirta la soo bandhigay
3. Schedule page — foomka ballan qabashada
4. Doctors page — liiska dhakhaatiirta
5. Appointment list page — liiska ballamaha
6. Contact page — foomka xiriirka
7. Dashboard page — (bogga login-ka ah ee tirakoobka)

## Log In / Log Out

- Isticmaalayaasha waxay ku soo gali karaan `/login/` iyo ka bixi `/logout/`
- Boggagga sida Dashboard, Patients, Schedule, Appointments waxay u baahan yihiin in user-ku uu login sameeyo (`@login_required`)

## Admin Page

Dhammaan models-ka (Doctor, Patient, Appointment) waxaa lagu diiwaan geliyay `admin.py` faylalka apps-ka, marka waxaad ka maamuli kartaa `/admin/`.
