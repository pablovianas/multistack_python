from ..forms.user_forms import UserForms, EditUserForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def user_register(request):
    if request.method == 'POST':
        user_form = UserForms(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = UserForms()

    return render(request, 'users/user_form.html', {'user_form': user_form})

@login_required
def user_list(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=True)
    return render(request, 'users/user_list.html', {'users': users})

@login_required
def edit_user(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)

    user_form = EditUserForm(request.POST or None, instance = user)

    if user_form.is_valid():
        user_form.save()
        return redirect('user_list')
    return render(request, 'users/user_form.html', {'user_form': user_form})
        
    

