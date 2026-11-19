from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients_list, name='patients_list'),
    path('add/', views.patient_add, name='patient_add'),
]
