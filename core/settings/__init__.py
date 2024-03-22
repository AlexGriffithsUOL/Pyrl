from .base import *
from dotenv import load_dotenv
import os

if ('ENV' in os.environ) == False:
    load_dotenv()

print('env', os.environ['ENV'])
print('env-2', ENV)

IS_HEROKU = 'IS_DYNO' in os.environ

if IS_HEROKU and ENV == ENV_STAGING:
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    from .prod import *
else:
    from .dev import *