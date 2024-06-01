from django import forms
from user_management.models import PyrlUser
from django.contrib.auth.models import User
from core.widgets import widgets

class SignUpForm(forms.ModelForm):
    class Meta:
        model=PyrlUser
        fields = ['first_name', 'last_name', 'mfa_enabled', 'mfa_type', 'mfa_code']
        field_names = ['First Name', 'Last Name', 'Password', 'Email', 'MFA Enabled', 'MFA Type', 'MFA Code']
        widgets = { 'password': forms.PasswordInput()}

class RootLoginForm(forms.ModelForm):
    class Meta:
        model=PyrlUser
        fields = ['email', 'password']
        field_names = ['Email', 'Password']
        widgets = { 'email': widgets['CustomInput'],
                    'password': widgets['CustomTextInput3']}