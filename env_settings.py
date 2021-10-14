'''
add this to the end of settings.py
env settings for containerization

try:
    from .env_settings import * 
except ImportError: 
    pass 
'''

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Get Django environment set by docker or use local
try:
    DJANGO_ENV = os.environ.get("DJANGO_ENV")
except:
    DJANGO_ENV = 'local'

#  env variable DJANGO_ENV set for development or production uses PostgreSQL
if DJANGO_ENV == 'development' or DJANGO_ENV == 'production':

    try:
        SECRET_KEY = os.environ.get("SECRET_KEY")
    except:
        SECRET_KEY = 'localsecret'

    try:
        DEBUG = int(os.environ.get("DEBUG", default=0))
    except:
        DEBUG = False

    try:
        ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
    except:
        ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("POSTGRES_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("POSTGRES_USER", "user"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        }
    }

# CORS rules
CORS_ORIGIN_ALLOW_ALL = True
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'