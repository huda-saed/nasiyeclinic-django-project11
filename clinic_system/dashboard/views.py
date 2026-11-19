from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


@login_required
def dashboard(request):
    context = {
        'total_patients': Patient.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'recent_appointments': Appointment.objects.select_related('doctor').all()[:5],
        'recent_patients': Patient.objects.all()[:5],
    }
    return render(request, 'dashboard/dashboard.html', context)
