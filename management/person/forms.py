from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person


class SignupForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_customer', 'is_employee')
