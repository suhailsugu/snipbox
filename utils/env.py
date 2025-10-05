import os

import environ
from dotenv import find_dotenv, load_dotenv

env = environ.Env(
    DEBUG=(bool, False),
)
load_dotenv(find_dotenv(), override=True, verbose=True)


def get_env_value(key, default=None):
    try:
        return env(key, default=default)
    except environ.ImproperlyConfigured:
        return os.environ.get(key, default)
