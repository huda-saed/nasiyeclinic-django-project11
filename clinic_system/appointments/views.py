from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm


@login_required
def schedule(request):
    """Schedule appointment page - Fullname, Appoint name, Time in, Time out, Date."""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ballanta si guul leh ayaa loo diiwaan geliyay!")
            return redirect('appoint_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule.html', {'form': form})


@login_required
def appoint_list(request):
    appointments = Appointment.objects.select_related('doctor').all()
    return render(request, 'appointments/appoint_list.html', {'appointments': appointments})
