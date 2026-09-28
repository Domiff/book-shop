"""
Environment variables (django-environ).
https://django-environ.readthedocs.io/
"""

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the backend/ directory, ROOT_DIR is the repository root.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_DIR = BASE_DIR.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ["localhost", "127.0.0.1"]),
    POSTGRES_NAME=(str, ""),
    POSTGRES_USER=(str, ""),
    POSTGRES_PASSWORD=(str, ""),
    POSTGRES_HOST=(str, "localhost"),
    POSTGRES_PORT=(str, "5432"),
    CSRF_TRUSTED_ORIGIN=(str, "http://127.0.0.1:8080"),
)

environ.Env.read_env(ROOT_DIR / ".env")
