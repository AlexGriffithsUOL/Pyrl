from django import forms
from .models import pyrl_user
from django.contrib.auth.models import User

# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model=pyrl_user
#         fields = ['id', 'first_name', 'last_name', 'password']
#         field_names = ['id', 'First Name', 'Last Name', 'Password']
#         widgets = { 'password': forms.PasswordInput()}

class SignUpForm(forms.ModelForm):
    class Meta:
        model=pyrl_user
        fields = ['first_name', 'last_name', 'mfa_enabled', 'mfa_type', 'mfa_code']
        field_names = ['First Name', 'Last Name', 'Password', 'Email', 'MFA Enabled', 'MFA Type', 'MFA Code']
        widgets = { 'password': forms.PasswordInput()}

class RootLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['email', 'password']
        field_names = ['Email', 'Password']
        widgets = { 'password': forms.PasswordInput()}