import imp
from unicodedata import name
from django.urls import path
from .views import service_register, service_list, edit_service

urlpatterns = [
    path('services/register', service_register, name="service_register"),
    path('services/list', service_list, name='service_list'),
    path('services/edit/<int:id>', edit_service, name='edit_service'),
]