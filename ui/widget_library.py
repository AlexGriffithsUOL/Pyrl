from django.forms import widgets

class WidgetMixin(object):
    class_options = {}
    
    def __init__(self, *args, **kwargs):
        super(WidgetMixin, self).__init__(*args, **kwargs)
        return
    
    def get_context(self, name, value, attrs, *args, **kwargs):
        context = super().get_context(name,value,attrs)
        context['widget']['class_options'] = self.class_options
        return context
    
class TestCustomWidget(WidgetMixin, widgets.TextInput):
    template_name = 'input.html'
    
class EmailWidget(WidgetMixin, widgets.EmailInput):
    template_name='email.html'
    
class PasswordWidget(WidgetMixin, widgets.PasswordInput):
    template_name = 'password.html'
    
class IntegerWidget(WidgetMixin, widgets.NumberInput):
    template_name = 'number.html'
    
class TestTextWidget(WidgetMixin, widgets.TextInput):
    template_name = 'text.html'