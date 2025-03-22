from django.urls import path, include
from . import views

CUSTOMERS_ENDPOINT = 'customers/'

urlpatterns = [
    path('customers/', view=views.ARGH.as_view()),
    path(CUSTOMERS_ENDPOINT + '<str:id>/', view=views.ARGH.as_view())
]