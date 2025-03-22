from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'projects'

urlpatterns = [
    path("details/<str:project_id>", view=views.ProjectDetailsView.as_view(), name="details"),
    path("create/", view=views.ProjectCreateView.as_view(), name="create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)