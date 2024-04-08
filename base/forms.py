from django import forms
from .models import pyrl_user

class SignUpForm(forms.ModelForm):
    class Meta:
        model=pyrl_user
        fields = ['id', 'first_name', 'last_name', 'password']
        field_names = ['id', 'First Name', 'Last Name', 'Password']
        widgets = { 'password': forms.PasswordInput()}