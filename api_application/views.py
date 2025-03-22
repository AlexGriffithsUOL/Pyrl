from django.shortcuts import render
from django.http import JsonResponse
from .models import ApiKey
from django.views import View

def construct_error_message(message, *args, **kwargs):
    return {
        'ERR': {
            'MSG': message
        }
    }

# Create your views here.
def ApiKeyWrapper(self, *Args, **kwargs):
    def wrapper(func, *args, **kwargs):
        if 'pyrl-api-key' not in func.request.headers:
            return JsonResponse(construct_error_message('No API Key in request headers'))
    return wrapper
    
        
class ARGH(View):
    
    @ApiKeyWrapper
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({'eee':'aaa'})