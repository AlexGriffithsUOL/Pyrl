from django.http import HttpResponseBadRequest
from django.shortcuts import redirect

def ajax_required(function):
    def wrap(request, *args, **kwargs):
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return redirect('four')
        return function(request, *args, **kwargs)
    return wrap