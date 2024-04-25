"""
Django settings for FarmerHouse project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'main/templates')
STATIC_DIR=os.path.join(BASE_DIR,'main/static')
MEDIA_ROOT=os.path.join(BASE_DIR,'main/media')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&i!*#x*g@hhuk3qp_uzbi0q-_gdnb==zvv^03#_c)l5*!i7sk+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    # Added.
    # 'keyboard_shortcuts',
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

ROOT_URLCONF = 'FarmerHouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'FarmerHouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         "NAME": os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Render postgresSQL database
import dj_database_url

RENDER_EXTERNAL_HOSTNAME = "postgres://farmer_house_user:zqcvVMH67J2QNvc87v7HfLxJqZsTckp5@dpg-cokro5md3nmc739kfc20-a.oregon-postgres.render.com/farmer_house"
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgres://farmer_house_user:zqcvVMH67J2QNvc87v7HfLxJqZsTckp5@dpg-cokro5md3nmc739kfc20-a.oregon-postgres.render.com/farmer_house',
        conn_max_age=600
    )
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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'main/static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#for Login sestyem
LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/login'

# START keyboard_shortcuts settings #
# HOTKEYS = [
#             {'keys': 'shift+s',  # go home
#             'link': '/AddSalesEntry'},
#             {'keys': 'shift+p',
#             'link': '/AddPurchaseEntry',},
#             {'keys': 'shift+i',
#             'link': '/AddProduct',},
#             {'keys': 'shift+a',
#             'link': '/UserAccount',},
#         ]
# SPECIAL_DISABLED = True
# END keyboard_shortcuts settings #

