from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('list/', views.appoint_list, name='appoint_list'),
]
