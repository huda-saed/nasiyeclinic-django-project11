from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'appoint_name', 'doctor', 'time_in', 'time_out', 'date']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname'}),
            'appoint_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Appoint name'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'time_in': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'time_out': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
