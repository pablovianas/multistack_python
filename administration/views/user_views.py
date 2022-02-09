from ..forms.user_forms import UserForms
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

def user_register(request):
    if request.method == 'POST':
        user_form = UserForms(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = UserForms()

    return render(request, 'users/user_form.html', {'user_form': user_form})

def user_list(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)
    return render(request, 'users/user_list.html', {'users': users})
