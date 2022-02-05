from django.shortcuts import render
from .forms import ServiceForm

# Create your views here.

def service_register(request):
    form_service = ServiceForm()
    return render(request, 'services/form_service.html', {'form_service': form_service})