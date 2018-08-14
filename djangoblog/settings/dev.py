from .base import *

ALLOWED_HOSTS = ['django-blog-humancode.c9users.io']

DEBUG = True



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}