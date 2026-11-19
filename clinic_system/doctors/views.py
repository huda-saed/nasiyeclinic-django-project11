from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Doctor


@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors_list.html', {'doctors': doctors})
