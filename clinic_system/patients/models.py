from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Lab'),
        ('F', 'Dhedig'),
    )

    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
