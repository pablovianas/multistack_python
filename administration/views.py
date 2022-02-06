from django.shortcuts import redirect, render
from .forms import ServiceForm
from .models import Service

# Create your views here.

def service_register(request):
    if request.method == 'POST':
        form_service = ServiceForm(request.POST)
        if form_service.is_valid():
            form_service.save()
            return redirect('service_list')
    else:
        form_service = ServiceForm()

    return render(request, 'services/form_service.html', {'form_service': form_service})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def edit_service(request, id):
    service = Service.objects.get(id=id)
    form_service = ServiceForm(request.POST or None, instance=service)
    if form_service.is_valid():
        form_service.save()
        return redirect('service_list')
    return render(request, 'services/form_service.html', {'form_service': form_service})