"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#x=hu30o(#sl9zy8po!(ghvcuza8#$rz5u586du4m$g1cq_#@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
dj_database_url
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoapp',
        'USER': 'django',
        'PASSWORD': 'se172fun',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Application definition

INSTALLED_APPS = [
    'login.apps.LoginConfig', #this is needed for each page/app
    'timecard.apps.TimecardConfig', #this is needed for each page/app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   # 'django_saml2_auth',
    'social_django',
    'EasyTimeCard',

]

SOCIAL_AUTH_TRAILING_SLASH = False                    # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'awesomepawesome.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'E61bFrD2I6Dm3M5DfsdZtzNwCuBPIx0U'
SOCIAL_AUTH_AUTH0_SECRET = 'Vgy_fW2X6QT_PxIYpzwuyNmnEvL2a7q2kWJScXNjbtBNduREEk30pGWYQ1tf8aBl'

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile'
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

AUTHENTICATION_BACKENDS = {
    'login.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/dashboard"
LOGOUT_REDIRECT_URL = "/"

METADATA_AUTO_CONF_URL = {

}
SAML2_AUTH = {
    # Required setting
    'METADATA_AUTO_CONF_URL': 'https://dev-492989.oktapreview.com/app/exkersxgxh5s8jm8l0h7/sso/saml/metadata',
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'shivangiagarwal53@gmail.com',
        'username': 'UserName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
    },
}

ROOT_URLCONF = 'EasyTimeCard.urls'

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

WSGI_APPLICATION = 'EasyTimeCard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)