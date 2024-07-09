from django.forms.widgets import Input, PasswordInput, TextInput, Textarea, EmailInput
from django.utils.safestring import SafeString
from django.forms.widgets import Widget
from django import forms


# Custom test widget input, replaces the INPUT inheritance
class CustomInputInput(Widget): 
    """
    Base class for all <input> widgets.
    """

    input_type = None  # Subclasses must define this.
    template_name = "widgets\input.html" # Test changing this to custom template
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
    


class CustomInput:
    is_hidden = False
    attrs = {}
    def use_required_attribute(self, *args, **kwargs):
        return

    def render(self, name, value, attrs=None, renderer=None):
        return SafeString(f'<input class="p-1 border border-black" />')

class CustomTextInput(TextInput):
    icon = ''
    def render(self, name, value, attrs=None, renderer=None):
        if self.icon:
            final_attrs = self.build_attrs(attrs)
            return SafeString(f'<div class="input-group"><span class="input-group-addon"><img src="{self.icon}" /></span>{super().render(name, value, final_attrs)}</div>')
        else:
            return super().render(name, value, attrs)
        
class CustomTextInput2(TextInput):
    icon = 'a'
    def render(self, name, value, attrs=None, renderer=None):
        if self.icon:
            final_attrs = self.build_attrs(attrs)
            return SafeString(f'<p>{self.icon}</p><div class="input-group"><span class="input-group-addon"><img src="{self.icon}" /></span>{super().render(name, value, final_attrs)}</div>')
        else:
            return super().render(name, value, attrs)
        
class CustomPasswordInput(CustomInputInput):
    value = 'Password'
    input_type = "text"
    template_name = "widgets/password.html"

class CustomEmailInput(CustomInputInput):
    value = 'Email'
    input_type = "email"
    classes = 'border-0 text-black dark:text-white bg-white dark:bg-gray-500'
    template_name = "widgets/email.html"

class newTestWidget(forms.EmailInput):
    template_name = 'widgets/email2.html'
