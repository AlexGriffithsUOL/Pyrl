from django.forms.widgets import Input, PasswordInput, TextInput, Textarea, EmailInput
from django.utils.safestring import SafeString
from django.forms.widgets import Widget
from django import forms
from django.utils.safestring import SafeString


# Custom test widget input, replaces the INPUT inheritance
class CustomInputInput(Widget): 
    """
    Base class for all <input> widgets.
    """

    input_type = None  # Subclasses must define this.
    template_name = "widgets\simple_input.html" # Test changing this to custom template
    classes = None
    styles = None
    value = None

    def __init__(self, attrs=None):
        if attrs is not None:
            attrs = attrs.copy()
            self.input_type = attrs.pop("type", self.input_type)
        super().__init__(attrs)
        # Sets up the template context for the widget.

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["type"] = self.input_type

        if self.styles:
            context['widget']['styles'] = self.styles
            print(self.styles)

        if self.classes:
            context['widget']['classes'] = self.classes
            print(context)

        if self.value:
            context['widget']['value'] = self.value
        
        return context    
    # Returns the context for the widget
    
class CustomClearingInput(CustomInputInput):
    template_name='widgets\cleraing_input.html'

class CustomInput:
    is_hidden = False
    attrs = {}
    def use_required_attribute(self, *args, **kwargs):
        return

    def render(self, name, value, attrs=None, renderer=None):
        return SafeString(f'<input class="p-1 border border-black" />')

        
        
class CustomPasswordInput(CustomInputInput):
    value = 'Password'
    input_type = "text"
    template_name = "widgets/password.html"

class CustomEmailInput(CustomInputInput):
    value = 'Email'
    input_type = "email"
    template_name = "widgets/large_email.html"

class CustomTextInput(CustomClearingInput):
    value = ''
    input_type = 'text'
    template_name = 'widgets/large_input.html'

class SignUpFormInputs:
    class FirstNameInput(CustomTextInput):
        value = 'First name(s)'
    
    class MiddleNamesInput(CustomTextInput):
        value = 'Middle name(s)'

    class LastNamesInput(CustomTextInput):
        value = 'Last name(s)'

    class EmailInput(CustomEmailInput):
        value = 'example@example.com'
    
    class PasswordInput(CustomPasswordInput):
        None

    class ConfirmPasswordInput(CustomPasswordInput):
        value='Confirm Password'

