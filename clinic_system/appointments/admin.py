from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'appoint_name', 'doctor', 'date', 'time_in', 'time_out')
    search_fields = ('full_name', 'appoint_name')
    list_filter = ('date', 'doctor')
