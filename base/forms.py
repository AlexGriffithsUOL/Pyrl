from django import forms
from .models import pyrl_users

class SignUpForm(forms.ModelForm):
    class Meta:
        model=pyrl_users
        fields = ['id', 'first_name', 'last_name', 'password']
        field_names = ['id', 'First Name', 'Last Name', 'Password']
        widgets = { 'password': forms.PasswordInput()}