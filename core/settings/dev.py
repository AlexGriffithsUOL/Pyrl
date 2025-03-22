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

PLAID_API_KEY=os.environ['PLAID_API_KEY']
PLAID_API_URL=os.environ['PLAID_API_URL']
PLAID_CLIENT_ID=os.environ['PLAID_CLIENT_ID']