import re
from base.models import PyrlClient
from django.contrib.sessions.models import Session
from django.utils.timezone import now

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

# class OneSessionPerUserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             current_session_key = request.session.session_key
#             user_sessions = Session.objects.filter(expire_date__gte=now())
#             for session in user_sessions:
#                 data = session.get_decoded()
#                 if data.get('_auth_user_id') == str(request.user.id) and session.session_key != current_session_key:
#                     session.delete()
#         return self.get_response(request)