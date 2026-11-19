from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.employee_register, name='employee_register'),
]
