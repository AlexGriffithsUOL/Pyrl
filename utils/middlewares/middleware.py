def determine_ajax(get_resposne):
    def middleware(request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            request.is_ajax = True
        else:
            request.is_ajax = False
            
        response = get_resposne(request)
        return response
    return middleware