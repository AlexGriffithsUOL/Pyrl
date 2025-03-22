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
    path("calendar/", include("jobs.urls")),
    path('customers/', include("customers.urls")),
    path('chart_of_accounts/', include('chart_of_accounts.urls')),
    path('projects/', include('projects.urls')),
    path('aws/', include('aws.urls')),
    path('transaction/', include('transaction.urls')),
    path("bank/", include("banking.urls")),
    path("auth/", include("user_management.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)