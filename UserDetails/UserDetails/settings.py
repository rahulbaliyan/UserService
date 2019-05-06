"""
Django settings for UserDetails project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

__author__ = "rahul"
__version__ ="1.0"
__date__ = "Jan 22 15:48:15 2019"
__copyright__ = "©2019 quadratyx"

"""

import os
import json
import environ


ROOT_DIR = environ.Path(__file__) - 2
env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env_file = str(ROOT_DIR.path('.env'))
    env.read_env(env_file)
DEBUG = False
ALLOWED_HOSTS = ["*"]
# config path variable
# global_config = os.environ['MORTGAGE_CONFIG_PATH']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read the configuration settings

microservicename = 'UserDetailsApp'
log_dir = env('LOG_DIR')
filename = microservicename + '.log'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mh=3vf0rm&87q9b9o_tnltc@cfsw$b*7c=1#*-m-2d5v#=d&*r'

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

# add application name in installed apps

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env('DB_NAME'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', cast=int),
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'UserDetailsApp',
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# define root url of project
ROOT_URLCONF = 'UserDetails.urls'


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

WSGI_APPLICATION = 'UserDetails.wsgi.application'

ADMINS = [('rkumar@quadratyx.com')]
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
print(env('DB_NAME'), env('DB_HOST'), env('DB_PORT'))



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# logging configuration
LOGGING = {
            'version': 1,
            'disable_existing_loggers': True,
            'filters': {
                    'require_debug_false': {
                        '()': 'django.utils.log.RequireDebugFalse'
                    }
                },
            'formatters': {
                'verbose': {
                    'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
                },
                'simple': {
                            'format': '%(levelname)s %(message)s'
                          },
                'standard': {
                    'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
                },
            },
             'handlers': {
                             'default': {
                                 'level': 'DEBUG',
                                 'class': 'logging.handlers.RotatingFileHandler',
                                 'filename': os.path.join(log_dir, filename),
                                 'maxBytes': 1024 * 1024 * 5,  # 5 MB
                                 'backupCount': 5,
                                 'formatter': 'standard',
                             },
                             'file': {
                                                    'level': 'DEBUG',
                                                    'filename': os.path.join(log_dir, filename),
                                                    'class': 'logging.FileHandler',
                                                    'formatter': 'verbose'
                                        },
                            'applogfile': {
                                            'level': 'INFO',
                                            'class': 'logging.FileHandler',
                                            'filename': os.path.join(log_dir, filename),
                                            'formatter': 'verbose'
                                          },
                            'mail_admins': {
                                        'level': 'ERROR',
                                        'filters': ['require_debug_false'],
                                        'class': 'django.utils.log.AdminEmailHandler'
                                    },
                                    'console': {
                                        'level': 'DEBUG',
                                        'class': 'logging.StreamHandler',
                                        'formatter': 'verbose',
                                    }

                            },
            'loggers': {
                            'UserDetailsApp': {
                                                    'handlers': ['applogfile', 'file', 'default'],
                                                    'level': 'DEBUG',
                                                    'propagate': True,
                                                },

                            'django.request': {
                                                'handlers': ['mail_admins'],
                                                'level': 'ERROR',
                                                'propagate': False,
                                            },
                            'django.security': {
                                                'handlers': ['mail_admins'],
                                                'level': 'ERROR',
                                                'propagate': False,
                                            },
                            'py.warnings': {
                                              'handlers': ['console'],
                                            },
                        },
}
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
# 'handlers': ['file', 'console','mail_admins'],
# time zone , we can change time zone according location
TIME_ZONE = 'UTC'


USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'