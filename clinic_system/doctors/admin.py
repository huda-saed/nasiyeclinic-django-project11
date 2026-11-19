from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialty', 'phone_number', 'email', 'created_at')
    search_fields = ('full_name', 'specialty', 'email')
    list_filter = ('specialty',)
