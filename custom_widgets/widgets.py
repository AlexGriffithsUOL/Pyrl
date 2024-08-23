from django.utils.safestring import SafeString
from django.forms.widgets import Widget
from django import forms
from django.template import loader
from django.utils.safestring import SafeString, mark_safe

# Custom test widget input, replaces the INPUT inheritance
class CustomInputInput(Widget): 
    """
    Base class for all <input> widgets.
    """

    input_type = None  # Subclasses must define this.
    template_name = "widgets/simple_input.html" # Test changing this to custom template
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
    template_name='widgets/cleraing_input.html'

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

class MyWidget(forms.Widget):
    template_name = 'fragments/widgets/select.html'
    input_type = "select"
    option_template_name = "fragments/widgets/select_option.html"
    add_id_index = False
    checked_attribute = {"selected": True}
    option_inherits_attrs = False
    allow_multiple_selected = False

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.allow_multiple_selected:
            context["widget"]["attrs"]["multiple"] = True
        return context

    def render(self, renderer, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
    
    @staticmethod
    def _choice_has_empty_value(choice):
        """Return True if the choice's value is empty string or None."""
        value, _ = choice
        return value is None or value == ""

    def use_required_attribute(self, initial):
        """
        Don't render 'required' if the first <option> has a value, as that's
        invalid HTML.
        """
        use_required_attribute = super().use_required_attribute(initial)
        # 'required' is always okay for <select multiple>.
        if self.allow_multiple_selected:
            return use_required_attribute

        first_choice = next(iter(self.choices), None)
        return (
            use_required_attribute
            and first_choice is not None
            and self._choice_has_empty_value(first_choice)
        )
    
class SelectInput(forms.Select):
    template_name = 'fragments/widgets/select.html'
    option_template_name = "fragments/widgets/select_option.html"

class DecimalInput(forms.DecimalField):
    template_name = 'fragments/widgets/decimal.html'
    allow_multiple_selected = False
    value = 0.00
    is_hidden = False
    attrs = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = 'fragments/widgets/decimal.html'

    def use_required_attribute(self, *args, **kwargs):
        return False

    def get_context(self, name, value, attrs):
        context = { 'attrs':attrs, 'name':name, 'value':value }
        if self.allow_multiple_selected:
            context["widget"]["attrs"]["multiple"] = True
        return context

    def render(self, renderer, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        print(self.template_name)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
    
class CurrencyInput(DecimalInput):
    template_name = 'fragments/widgets/currency.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = 'fragments/widgets/currency.html'