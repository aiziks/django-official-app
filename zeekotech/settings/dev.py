from .base import *
from decouple import config



SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = []