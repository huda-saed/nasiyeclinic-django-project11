from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Fullname")
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
