"""
Django settings for media_scrap project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!72fhxk&9_m3dg1g7mw_kls%%b+4z5psm$wrguun-u&ku4rf!='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'core',
    'playground',
    'register',
    'youtube',
    'debug_toolbar'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

ROOT_URLCONF = 'media_scrap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'media_scrap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MONGODB = {
    'DB_NAME': 'youtube',
    'USER': 'mediascrap',
    'PASSWORD': 'tjdrhd05Aa!',
    'HOST': '127.0.0.1',
    'PORT': '27017',
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

AUTH_USER_MODEL = 'core.User'

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'current_user': 'core.serializers.UserSerializer',
    }
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1)
}

CELERY_BROKER_URL = 'redis://localhost:6379/1'

# Define the list of keywords to be processed consecutively
KEYWORDS_1 = ['캠핑','먹방','여행','요리','자동차']
KEYWORDS_2 = ['뉴스','주식','정치','경제','사회']
KEYWORDS_3 = ['문화','역사','시사','생활','애완']
KEYWORDS_4 = ['프로그램','어린이','미용','건강','패션']
KEYWORDS_5 = ['연예','스포츠','kpop','영화','음악','골프']


# Define the Celery Beat schedule
CELERY_BEAT_SCHEDULE = {
    'execute_keyword_tasks1': {
        'task': 'playground.tasks.run_scrap_channels',
        # Define the schedule for the task (e.g., run every hour)
        'schedule': crontab(hour=1, minute=0, day_of_week=1),  # Run at 1:00 AM every Monday
        # Pass the list of keywords as an argument to the task
        'args': (KEYWORDS_1,),
    },
    'execute_keyword_tasks2': {
        'task': 'playground.tasks.run_scrap_channels',
        # Define the schedule for the task (e.g., run every hour)
        'schedule': crontab(hour=1, minute=0, day_of_week=2),  # Run at 1:00 AM every Monday
        # Pass the list of keywords as an argument to the task
        'args': (KEYWORDS_2,),
    },
    'execute_keyword_tasks3': {
        'task': 'playground.tasks.run_scrap_channels',
        # Define the schedule for the task (e.g., run every hour)
        'schedule': crontab(hour=1, minute=0, day_of_week=3),  # Run at 1:00 AM every Monday
        # Pass the list of keywords as an argument to the task
        'args': (KEYWORDS_3,),
    },
    'execute_keyword_tasks4': {
        'task': 'playground.tasks.run_scrap_channels',
        # Define the schedule for the task (e.g., run every hour)
        'schedule': crontab(hour=1, minute=0, day_of_week=4),  # Run at 1:00 AM every Monday
        # Pass the list of keywords as an argument to the task
        'args': (KEYWORDS_4,),
    },
    'execute_keyword_tasks5': {
        'task': 'playground.tasks.run_scrap_channels',
        # Define the schedule for the task (e.g., run every hour)
        'schedule': crontab(hour=1, minute=0, day_of_week=5),  # Run at 1:00 AM every Monday
        # Pass the list of keywords as an argument to the task
        'args': (KEYWORDS_5,),
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}