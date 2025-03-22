from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'customers'

urlpatterns = [
    path("list/", view=views.CustomerListView.as_view(), name="list"),
    path("<int:customer_id>/details/", view=views.CustomerDetailsView.as_view(), name="details"),
    path("<int:customer_id>/contacts/add/", view=views.CustomerAddEditContact.as_view(), name='add-contact'),
    path("<int:customer_id>/contacts/<int:contact_id>/edit/", view=views.CustomerAddEditContact.as_view(), name='edit-contact'),
    path("create/", view=views.CustomerCreateView.as_view(), name="create"),
    path("groups/list/", view=views.CustomerGroupListView.as_view(), name="list-groups"),
    path("groups/create/", view=views.CustomerGroupCreateView.as_view(), name="create-groups"),
    path("activate/<str:customer_contact_uuid>/", view=views.CustomerContactActivationView.as_view(), name="contact-activate")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)