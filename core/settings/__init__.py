from .base import *
from dotenv import load_dotenv

import os

load_dotenv()
ENV = os.environ['ENV']

print(f'Running in {ENV} environment')

IS_HEROKU = 'IS_DYNO' in os.environ

if IS_HEROKU and ENV == ENV_STAGING:
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    from .prod import *
else:
    from .dev import *