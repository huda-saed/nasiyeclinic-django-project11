from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import StyledUserCreationForm
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment


def home(request):
    """Homepage with a hero carousel of 3 images and quick clinic info."""
    featured_doctors = Doctor.objects.all()[:3]
    context = {
        'featured_doctors': featured_doctors,
        'total_doctors': Doctor.objects.count(),
        'total_patients': Patient.objects.count(),
        'total_appointments': Appointment.objects.count(),
    }
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == 'POST':
        messages.success(request, "Fariintaada waa la helay! Waan kula soo xiriiri doonaa dhawaan.")
        return redirect('contact')
    return render(request, 'core/contact.html')


def register(request):
    if request.method == 'POST':
        form = StyledUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Akoonkaaga waa la abuuray! Ku soo dhowow.")
            return redirect('dashboard')
    else:
        form = StyledUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
