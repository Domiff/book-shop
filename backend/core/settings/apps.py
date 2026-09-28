"""
Application definition.
https://docs.djangoproject.com/en/5.2/ref/settings/#installed-apps
"""

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "books.apps.BooksConfig",
    "api.apps.ApiConfig",
    "auth_user.apps.AuthUserConfig",
]
