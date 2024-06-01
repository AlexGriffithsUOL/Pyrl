from .base import *
import os

IS_HEROKU = 'DYNO' in os.environ

if IS_HEROKU and ENV == ENV_STAGING:
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    from .prod import *
else:
    from .dev import *