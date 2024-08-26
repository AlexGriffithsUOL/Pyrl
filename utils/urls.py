from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'utils'

urlpatterns = [
    path("messages/<str:status>/<str:encoded_message>/", view=views.retrieve_message, name="messages"),
    path("clear_messages/", view=views.clear_messages, name='clear_message')
]
