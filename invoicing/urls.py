from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'invoicing'

urlpatterns = [
    path("", view=views.InvoicingMainView.as_view(), name="index"),
    # path("create/", view=views.create_invoice.as_view(), name="create"),
    path("get_row/<str:fragment_id>", view=views.get_row, name="get_row"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)