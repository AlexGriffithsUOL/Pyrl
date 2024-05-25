from .base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR
import environ
import os

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(', ')

INSTALLED_APPS.append('whitenoise.runserver_nostatic')
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

DEBUG = os.environ['DEBUG']

SECRET_KEY = os.environ['SECRET_KEY']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Whitenoise
# https://whitenoise.evans.io/en/stable/django.html

DATABASES = {
    'default': environ.Env().db(),
}
