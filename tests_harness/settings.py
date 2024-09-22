DEBUG = True
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fake-key-for-testing'

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django_uswds',
]

MIDDLEWARE = []

ROOT_URLCONF = 'tests_harness.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['tests_harness/templates','django_uswds/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    ("uswds", BASE_DIR / "django_uswds/vendor/dist")
]

WSGI_APPLICATION = 'tests_harness.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

