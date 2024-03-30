from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", view=views.login.as_view(), name="login"),
    path("register/", view=views.register.as_view(), name="register"),
    path("create", view=views.create, name="create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)