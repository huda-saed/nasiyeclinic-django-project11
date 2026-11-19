from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'date_of_birth', 'phone_number', 'email')
    search_fields = ('full_name', 'phone_number', 'email')
    list_filter = ('gender',)
