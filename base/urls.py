from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'base'

urlpatterns = [
    path("", view=views.HomePageMainView.as_view(), name="index"),
    path("financial_product/", view=views.HomePageFinancialProductView.as_view(), name="finance_product"),
    path("stock_product/", view=views.HomePageStockProductView.as_view(), name="stock_product"),
    path("communication_product/", view=views.HomePageCommunicationProductView.as_view(), name="communication_product"),
    path("project_product/", view=views.HomePageProjectProductView.as_view(), name="project_product"),
    path("pricing/", view=views.HomePagePricingView.as_view(), name="pricing"),
    path("about/", view=views.HomePageAboutView.as_view(), name="about"),
    path("contact/", view=views.HomePageContactView.as_view(), name="contact"),
    # path("auth/", include("user_management.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)