from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'

urlpatterns = [
    path("view/", view=views.ProductMainView.as_view(), name="view"),
    path("new_product/", view=views.AsyncGetCreateNewProductHTMLFunc, name="new_product"),
    path("categories/", view=views.ProductCategoriesView.as_view(), name="categories"),
    path("create/", view=views.AsyncCreateProduct, name="create"),
    path("delete/", view=views.AsyncDeleteProduct, name="delete"),
    path("edit/", view=views.AsyncEditProduct, name="edit"),
    path("product_info/", view=views.AsyncGetProductInfo, name="product_info"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)