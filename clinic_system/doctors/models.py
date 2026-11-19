from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return f"Dr. {self.full_name} ({self.specialty})"
