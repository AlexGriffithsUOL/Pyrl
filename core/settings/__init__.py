from .base import *
from dotenv import load_dotenv
import os

print(os.environ)

if ('ENV' in os.environ) == False:
    load_dotenv()

print('env', os.environ['ENV'])
print('env-2', ENV)

IS_HEROKU = 'DYNO' in os.environ

print('IS_HEROKU', IS_HEROKU)

if IS_HEROKU and ENV == ENV_STAGING:
    print('Importing staging')
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    print('Importing prod')
    from .prod import *
else:
    print('Importing dev')
    from .dev import *