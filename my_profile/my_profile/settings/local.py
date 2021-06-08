from .base import *


# DEBUG = False

# ALLOWED_HOSTS = ["*", "api.odds.team", "52.192.11.105"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}