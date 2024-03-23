from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'base'

urlpatterns = [
    path("", view=views.index.as_view(), name="index"),
    path("pricing", view=views.pricing.as_view(), name="pricing"),
    path("about", view=views.about.as_view(), name="about"),
    path("contact", view=views.contact.as_view(), name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)