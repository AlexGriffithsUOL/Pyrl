from .base import *

NPM_BIN_PATH = "C://Users//dialg//AppData//Roaming//nvm//v20.0.0//npm.cmd"

INSTALLED_APPS.append('django_browser_reload')
MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")