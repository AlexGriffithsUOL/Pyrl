from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString

register = template.Library()

alert_choices = {
    'success': 'fragments/alerts/success_alert.html',
    'danger': 'fragments/alerts/danger_alert.html',
    'warning': 'fragments/alerts/warning_alert.html',
    'info': 'fragments/alerts/info_alert.html',
    'dark': 'fragments/alerts/dark_alert.html'
}

def get_alert(value, SafeString=SafeString):
    choice = alert_choices[value]
    return f'{SafeString(choice)}'

register.filter('get_alert', get_alert)