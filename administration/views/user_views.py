from ..forms.user_forms import UserForms
from django.shortcuts import render


def user_register(request):
    if request.method == 'POST':
        user_form = UserForms(request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserForms()

    return render(request, 'usuarios/user_form.html', {'user_form': user_form})