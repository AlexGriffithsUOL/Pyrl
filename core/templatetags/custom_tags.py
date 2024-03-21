from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString

register = template.Library()

@stringfilter
def get_setting(value, SafeString=SafeString):
    return getattr(settings, SafeString(value), "")

register.filter('get_setting', get_setting)