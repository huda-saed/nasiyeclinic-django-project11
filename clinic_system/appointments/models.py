from django.db import models
from doctors.models import Doctor


class Appointment(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Fullname")
    appoint_name = models.CharField(max_length=200, verbose_name="Appoint name")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    time_in = models.TimeField(verbose_name="Time in")
    time_out = models.TimeField(verbose_name="Time out")
    date = models.DateField(verbose_name="Date")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time_in']

    def __str__(self):
        return f"{self.full_name} - {self.appoint_name} ({self.date})"
