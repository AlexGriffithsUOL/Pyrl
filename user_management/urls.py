from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user_management'

urlpatterns = [
    path("signup/", view=views.UserManagementSignUpView.as_view(), name="signup"),
    path("login/", view=views.UserManagementLoginView.as_view(), name="login"),
    path("logout", view=views.LogOutFunc, name="logout"),
    path("dashboard/", view=views.AdminDashboardView.as_view(), name="admin_dashboard"),
    path("change_password/", view=views.UserManagementChangePasswordView.as_view(), name="change_password"),
    path("forgot_password/", view=views.UserManagementForgotPasswordView.as_view(), name="forgot_password"),
    path("users/list/", view=views.ListUserView.as_view(), name='list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)