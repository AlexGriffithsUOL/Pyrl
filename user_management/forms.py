from django import forms
from user_management.models import PyrlUser
from django.contrib.auth.models import User
from ui.widget_library import TestCustomWidget, PasswordWidget, EmailWidget

class SignUpForm(forms.ModelForm):
    class Meta:
        model=PyrlUser
        fields = ['first_name','middle_names', 'last_name', 'email']
        field_names = ['First Name', 'Middle Names', 'Last Name', 'Email']
        widgets = { 'password': TestCustomWidget(),
                    'first_name': TestCustomWidget(),
                    'middle_names': TestCustomWidget(),
                    'last_name': TestCustomWidget(),
                    'email': TestCustomWidget(),
                    'confirm_password': TestCustomWidget()
                   }
        
class FullSignupForm(SignUpForm):
    password=forms.CharField(widget=TestCustomWidget())
    confirm_password=forms.CharField(widget=TestCustomWidget())

    class Meta(SignUpForm.Meta):
        widgets = SignUpForm.Meta.widgets

class RootLoginForm(forms.ModelForm):
    class Meta:
        model=PyrlUser
        fields = ['email', 'password']
        field_names = ['Email', 'Password']
        widgets = { 'email': EmailWidget(attrs={'label':'Email'}),
                    'password': PasswordWidget(attrs={'label':'Password'})}
        
        labels ={
            'email': '',
            'password': ''
        }