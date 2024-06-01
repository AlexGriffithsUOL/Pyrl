from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main_app'

urlpatterns = [
    path("", view=views.dashboard.as_view(), name="index"),
    path("products/", include("products.urls")),
    path("invoice/", include("invoicing.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)