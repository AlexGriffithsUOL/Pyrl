import re
from base.models import PyrlClient

def add_parent_client_to_request(get_response):
    def middleware(request):
        if len(request.POST) > 0: #Somehow was causing posts to come through empty
            return get_response(request)
        if request.user.is_anonymous is False:
            if 'client' not in request:
                parent_client = PyrlClient.objects.get(client_id=request.user.client_id)
                request.client = parent_client
                request.user.client_id = parent_client.client_id
        return get_response(request) 
    return middleware