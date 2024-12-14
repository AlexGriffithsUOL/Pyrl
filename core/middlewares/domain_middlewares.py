import re
from base.models import PyrlClient
from django.shortcuts import redirect
from core.settings import MAIN_PAGE_PATH_ID
from core.settings import DOMAIN_PATHS

def  print_domain(get_response):
    def middleware(request):
        # return get_response(request)
        request_domain = request.headers['Host'].split(':')[0]
            
        if 'home' in request.path or 'reload' in request.path or request.path == '/' or '404' in request.path:
            if PyrlClient.objects.filter(domain=request_domain) and '404' not in request.path:
                if request.user.is_authenticated:
                    return redirect('main_app:index')
                
                return redirect('user_management:login')
            
            return get_response(request)
            
        if PyrlClient.objects.filter(domain=request_domain) or request.user.is_authenticated:
            return get_response(request)    
        
        return redirect('four')

    return middleware

# def add_parent_client_to_request(get_response):
#     def middleware(request):
#         if len(request.POST) > 0: #Somehow was causing posts to come through empty
#             return get_response(request)
#         if request.user.is_anonymous is False:
#             if 'client' not in request:
#                 parent_client = PyrlClient.objects.get(client_id=request.user.client_id)
#                 request.client = parent_client
#                 request.user.client_id = parent_client.client_id
#         return get_response(request) 
#     return middleware