import re
from django.conf import settings 
from datetime import datetime
from time import time
from uuid import uuid4
from analytics.models import request_analytics

def user_navigation_analytics(get_response):
    def middleware(request):
        user = request.user.id
        request_session = request.session.session_key
        requested_page = request.path
        enter_page_time = datetime.now()
        response = get_response(request)
        return response
    return middleware

def get_request_analytics(get_response):
    def middleware(request):
        valid_day = datetime.today().weekday() in settings.ANALYTICS_CONFIG['VALID_WEEKDAYS']
        if valid_day:
            requested_page = request.path

            truth_list = []
            for item in settings.NO_ANALYTICS:
                if requested_page in item:
                    truth_list.append(True)
                else:
                    truth_list.append(False)
                    
            truth_list = max(truth_list)

            if truth_list == False:
                request_id = uuid4()
                enter_response = time()
                response = get_response(request)
                exit_response = time()
                exec_time = exit_response - enter_response
                request_analytics.objects.create(request_id=request_id, request_time=exec_time, request_page=requested_page)
                return response
        response = get_response(request)
        return response
    return middleware