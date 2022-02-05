import imp
from unicodedata import name
from django.urls import path
from .views import service_register

urlpatterns = [
    path('services/register', service_register, name="service_register")
]