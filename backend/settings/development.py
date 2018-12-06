from .core import *

SECRET_KEY = "+1012sfpn)3c&l-)j!nyb(jog)w2c)tk5_#zygrcd&^3n8j3i5"
Debug = True
ALLOWED_HOSTS = ["*"]

# Just use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

