from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        print(username)
        login_valid = username == 'alex.john.griffiths.2001@gmail.com'
        pwd_valid = check_password(password, 'aaaa')
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        print('eeee')
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None