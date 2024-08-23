import re
from base.models import company

def add_company_to_request(get_response):
    def middleware(request):
        if request.user.is_anonymous is False:
            if 'client' not in request:
                user_company = company.objects.get(id=request.user.company_id)
                request.client = user_company
                request.user.company_id = user_company.id
                response = get_response(request)
                return response
        response = get_response(request)
        return response
    return middleware