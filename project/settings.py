from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import sys, os

#Localização dos Aplicativos Internos
sys.path.append(
    os.path.join(BASE_DIR, "apps")
)

SECRET_KEY = str(os.environ.get('SECRET_KEY', "django-insecure-900u2i6xbp12y#l7-%ch9h(w(jxj17n)c1btv1p=$6$iz27t7m"))

DEBUG = int(os.environ.get('DEBUG', 1))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'posts-django.herokuapp.com']

INTERNAL_IPS = ('*')

# APP's Padrões
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# APP's Externas
INSTALLED_APPS += [
    'bootstrap5',
]

# APP's Internas
INSTALLED_APPS += [
    'home',
    'users',
    'votations'
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# TimeOut Database
DATABASE_OPTIONS = {'timeout': 120}

DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.environ.get('DB_NAME', BASE_DIR / 'db.sqlite3')),
        'USER': str(os.environ.get('DB_USER', '')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD', '')),
        'HOST': str(os.environ.get('DB_HOST', '')),
        'PORT': str(os.environ.get('DB_PORT', ''))
    }
}

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: False if request.is_ajax() else True,
    }

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

AUTH_USER_MODEL = "users.User"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#SMTP
EMAIL_BACKEND = str(os.environ.get('EMAIL_BACKEND', "django.core.mail.backends.console.EmailBackend"))
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.environ.get('EMAIL_HOST_USER', ""))
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD', ""))
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Posts'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')