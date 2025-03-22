from django import forms
from django.forms.widgets import DateInput

class ProjectForm(forms.ModelForm):
    class Meta:
        from .models import Project
        model = Project
        fields = [
            'project_name',
            'customer'
        ]