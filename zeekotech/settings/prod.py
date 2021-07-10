from .base import *

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = []