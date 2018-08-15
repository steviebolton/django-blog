# SECURITY WARNING: don't run with debug turned on in production!
from .base import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['dev-meerewijck-chat-app.herokuapp.com']

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
