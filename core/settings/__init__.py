from .base import *
from dotenv import load_dotenv
import os

if ('ENV' in os.environ) == False:
    load_dotenv()

print('env', os.environ['ENV'])
print('env-2', ENV)

IS_HEROKU = 'IS_DYNO' in os.environ

if IS_HEROKU and ENV == ENV_STAGING:
    print('Importing staging')
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    print('Importing prod')
    from .prod import *
else:
    print('Importing dev')
    from .dev import *

print(INSTALLED_APPS)