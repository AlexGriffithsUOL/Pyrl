from django import forms
from user_management.models import PyrlUser
from django.contrib.auth.models import User
from core.widgets import widgets
from custom_widgets.widgets import SignUpFormInputs

class SignUpForm(forms.ModelForm):
    class Meta:
        model=PyrlUser
        fields = ['first_name','middle_names', 'last_name', 'email']
        field_names = ['First Name', 'Middle Names', 'Last Name', 'Email']
        widgets = { 'password': SignUpFormInputs.PasswordInput,
                    'first_name': SignUpFormInputs.FirstNameInput,
                    'middle_names': SignUpFormInputs.MiddleNamesInput,
                    'last_name': SignUpFormInputs.LastNamesInput,
                    'email': SignUpFormInputs.EmailInput,
                    'confirm_password': SignUpFormInputs.ConfirmPasswordInput
                   }
        
class FullSignupForm(SignUpForm):
    password=forms.CharField(widget=SignUpFormInputs.PasswordInput)
    confirm_password=forms.CharField(widget=SignUpFormInputs.ConfirmPasswordInput)

    class Meta(SignUpForm.Meta):
        widgets = SignUpForm.Meta.widgets

class RootLoginForm(forms.ModelForm):
    class Meta:
        model=PyrlUser
        fields = ['email', 'password']
        field_names = ['Email', 'Password']
        widgets = { 'email': widgets['CustomEmailInput'],
                    'password': widgets['CustomPasswordInput']}