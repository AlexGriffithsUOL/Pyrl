from .base import *
from dotenv import load_dotenv
import os

print(os.environ)

if ('ENV' in os.environ) == False:
    load_dotenv()

IS_HEROKU = 'DYNO' in os.environ

if IS_HEROKU and ENV == ENV_STAGING:
    print('Importing staging')
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    print('Importing prod')
    from .prod import *
else:
    print('Importing dev')
    from .dev import *