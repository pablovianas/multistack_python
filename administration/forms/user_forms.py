
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class UserForms(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.is_superuser = True
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class EditUserForm(UserChangeForm):
    password = None
    email = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name']
        exclude = ('password1', 'password2',)