from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'

urlpatterns = [
    path("view/", view=views.view_products.as_view(), name="view"),
    path("new_product/", view=views.new_product, name="new_product"),
    path("create/", view=views.create, name="create"),
    path("delete/", view=views.delete, name="delete"),
    path("product_info/", view=views.product_info, name="product_info"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)