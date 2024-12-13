from django.shortcuts import redirect
from django.conf import settings

class UserAuthenticatedMixin:
    """
    Ensures the user is authenticated. If not, redirects to the login page.
    """
    login_url = settings.LOGIN_URL  # Default to the project's LOGIN_URL setting

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
    
