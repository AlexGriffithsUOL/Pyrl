from django.template.loader import render_to_string
from uuid import uuid4
from django.http import JsonResponse

# Create your views here.
def retrieve_message(status, message, *args, **kwargs):
    template = "fragments/utils/messages"
    match (status):
        case 'ERR':
            template = f'{template}/error.html'
        case 'INF':
            template = f'{template}/info.html'
        case 'WAR':
            template = f'{template}/warning.html'
        case _:
            template = f'{template}/error.html'

    if 'length_of_time' in kwargs:
        length_of_time = kwargs.pop('length_of_time')
        length_of_time *= 1000
    else:
        length_of_time = 10 * 1000
    
    context = {'message':message, 'identifier':uuid4(), 'length_of_time': length_of_time}
    return render_to_string(template, context)

def clear_messages(request):
    if request.session['message'] and request.method=='POST':
        request.session['message'] = ''
        return JsonResponse({})
    
class message_manager:
    class STATUS:
        ERROR = 'ERR'
        WARNING = 'WAR'
        INFO = 'INF'

    def attach_message(request, status, message, *args, **kwargs):
        if 'length_of_time' in kwargs:
            length_of_time = kwargs.pop('length_of_time')
        else:
            length_of_time = 10
        rendered = retrieve_message(status, message, length_of_time=length_of_time)
        request.session['message'] = rendered