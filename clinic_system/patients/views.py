from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient
from .forms import PatientForm


@login_required
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients': patients})


@login_required
def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bukaanka waa la daray si guul leh!")
            return redirect('patients_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})
