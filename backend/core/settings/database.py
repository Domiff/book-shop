"""
Database settings.
https://docs.djangoproject.com/en/5.2/ref/settings/#databases
"""

from .env import ROOT_DIR, env

if env("DEBUG"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ROOT_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("POSTGRES_NAME"),
            "USER": env("POSTGRES_USER"),
            "PASSWORD": env("POSTGRES_PASSWORD"),
            "HOST": env("POSTGRES_HOST"),
            "PORT": env("POSTGRES_PORT"),
        }
    }
