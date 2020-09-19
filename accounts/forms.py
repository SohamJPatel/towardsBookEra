from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Member, MemberProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_no', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_no']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['profile_image', 'date_of_birth']