from .base import *
import os

IS_HEROKU = 'DYNO' in os.environ

if 'MAINTENANCE' in os.environ:
    MAINTENANCE = True
else:
    MAINTENANCE = True

if IS_HEROKU and ENV == ENV_STAGING:
    from .staging import *
elif IS_HEROKU and ENV == ENV_PROD:
    from .prod import *
elif IS_HEROKU is False and ENV == ENV_DEV:
    from .dev import *
else:
    raise Exception('Environment not found in __init__')