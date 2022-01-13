import environ

from projetoweb2.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOTS")

DATABASES = {
    "default": env.db(),
}