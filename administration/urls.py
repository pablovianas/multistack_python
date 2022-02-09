import imp
from unicodedata import name
from django.urls import path
from .views import service_views, user_views

urlpatterns = [
    path('services/register', service_views.service_register, name="service_register"),
    path('services/list', service_views.service_list, name='service_list'),
    path('services/edit/<int:id>', service_views.edit_service, name='edit_service'),
    path('user/register', user_views.user_register, name='user_register'),
    path('user/list', user_views.user_list, name='user_list'),
]