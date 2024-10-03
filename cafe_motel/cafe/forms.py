from django import forms
from .models import Booking, Sklad
from django.contrib.auth.forms import AuthenticationForm
from django.db import models

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'room', 'user_name', 'contact_info']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))

class ReceiveProductForm(forms.ModelForm):
    class Meta:
        model = Sklad
        fields = ['prod_name', 'kol_vo', 'edin']
        labels = {
            'prod_name': 'Название', 
            'kol_vo': 'Количество', 
            'edin': 'Единицы измерения',
        }

class Otgruz(forms.ModelForm):
    class Meta:
        model = Sklad
        fields = ['prod_name', 'kol_vo']
        labels = {
            'prod_name': 'Название', 
            'kol_vo': 'Количество', 
        }