from .base import *

try:
    from .npm_base import NPM_BASE
except:
    raise FileNotFoundError('npm_base.py not found in settings, if fresh install then download npm, and set NPM_BASE = the_installed_npm_path')

NPM_BIN_PATH = NPM_BASE

DEBUG = True

if RELOAD == True:
    INSTALLED_APPS.append('django_browser_reload')
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

DOMAIN_PATHS['local_reload'] = 'reload'