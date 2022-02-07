from unicodedata import decimal
from django import forms
from .models import Service
from decimal import Decimal

class ServiceForm(forms.ModelForm):
    min_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    porcentage_comission = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    value_bedroom = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    value_room = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    value_bathroom = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    value_kitchen = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    value_yard = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    value_others = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))

    class Meta:
        model = Service
        fields = '__all__'

    def clean_min_value(self):
        data = self.cleaned_data['min_value']
        return Decimal(data.replace(',','.'))

    def clean_porcentage_comission(self):
        data = self.cleaned_data['porcentage_comission']
        return Decimal(data.replace(',','.'))

    def clean_value_bedroom(self):
        data = self.cleaned_data['value_bedroom']
        return Decimal(data.replace(',','.'))

    def clean_value_room(self):
        data = self.cleaned_data['value_room']
        return Decimal(data.replace(',','.'))

    def clean_value_bathroom(self):
        data = self.cleaned_data['value_bathroom']
        return Decimal(data.replace(',','.'))

    def clean_value_kitchen(self):
        data = self.cleaned_data['value_kitchen']
        return Decimal(data.replace(',','.'))

    def clean_value_yard(self):
        data = self.cleaned_data['value_yard']
        return Decimal(data.replace(',','.'))

    def clean_value_others(self):
        data = self.cleaned_data['value_others']
        return Decimal(data.replace(',','.'))