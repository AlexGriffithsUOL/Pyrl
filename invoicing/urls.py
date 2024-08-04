from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'invoicing'

urlpatterns = [
    path("", view=views.index.as_view(), name="index"),
    path("pdf/<str:company_id>", view=views.pdf_generator, name="pdf_generator")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)