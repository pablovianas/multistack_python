from django.shortcuts import redirect, render
from ..forms.service_forms import ServiceForm
from ..models import Service
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def service_register(request):
    if request.method == 'POST':
        form_service = ServiceForm(request.POST)
        if form_service.is_valid():
            form_service.save()
            return redirect('service_list')
    else:
        form_service = ServiceForm()

    return render(request, 'services/form_service.html', {'form_service': form_service})

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def edit_service(request, id):
    service = Service.objects.get(id=id)
    form_service = ServiceForm(request.POST or None, instance=service)
    if form_service.is_valid():
        form_service.save()
        return redirect('service_list')
    return render(request, 'services/form_service.html', {'form_service': form_service})