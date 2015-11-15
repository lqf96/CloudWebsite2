"""
Django settings for CloudWebsite project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# Site sensitive secret
from CloudWebsite.sensitive_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Allowed hosts
ALLOWED_HOSTS = ["www.thcloud.ml","thcloud.ml"]

# Application definition
INSTALLED_APPS = (
    # Django applications
    # (May be replaced by xadmin in future)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django xadmin
    #'xadmin',
    #'crispy_forms',
    # Project applications
    'main',
)

# Middleware definition
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'CloudWebsite.urls'

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

# WSGI application
WSGI_APPLICATION = "CloudWebsite.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# (SQLite3 is used for debugging, while MySQL will be used in production)
DATABASES = {
    "default":{
        "ENGINE":"django.db.backends.sqlite3",
        "NAME":os.path.join(BASE_DIR,"db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR,"AdminStatic")

# Mail settings
EMAIL_HOST = "smtp.163.com"
EMAIL_USE_TLS = True

# Discourse site informations
DISCOURSE_BASE_URL = "https://forum.thcloud.ml"

# Insecure content proxy address
ICP_ADDR = "https://thcws.sinaapp.com/icp/"
