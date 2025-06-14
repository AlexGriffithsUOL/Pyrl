"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings import ENV, ENV_DEV, MAINTENANCE
from . import views

if MAINTENANCE:
    urlpatterns = [
        path("", view=views.maintenance.as_view(), name="maintenance")
    ]
else:
    urlpatterns = [
        path("", view=views.index.as_view(), name="index"),
        path("admin/", admin.site.urls),
        path("home/", include("base.urls")),
        path("main_app/", include("main_app.urls")),
        path("auth/", include("user_management.urls")),
        path("404/", view=views.FourOhFourView.as_view(), name="four"),
        path("utils/", include('utils.urls')),
    ]

    if ENV == ENV_DEV and settings.RELOAD:
        urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))

    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
