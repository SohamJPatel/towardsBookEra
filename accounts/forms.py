from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Member


class RegisterForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_no', 'password1', 'password2']
