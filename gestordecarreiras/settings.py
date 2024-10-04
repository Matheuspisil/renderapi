from pathlib import Path
import os
import dj_database_url
from django.db import migrations

def enable_autovacuum(apps, schema_editor):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute('ALTER TABLE my_table SET (autovacuum_enabled = true);')

class Migration(migrations.Migration):
    dependencies = [
        ('my_app', 'previous_migration'),
    ]

    operations = [
        migrations.RunPython(enable_autovacuum),
    ]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#definindo nosso usuario personalizado
AUTH_USER_MODEL = 'GPC.CustomUser'
USERNAME_FIELD = 'email'

#Redirecionamento de autenticacao do Django
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'index'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "tec21boss")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG","False").lower() == "True"

ALLOWED_HOSTS=['blackestech.com.br','127.0.0.1','localhost']




# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'GPC',
    'django_bootstrap5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'gestordecarreiras.middleware.DisableStaticCacheMiddleware',
]

ROOT_URLCONF = "gestordecarreiras.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS":  [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gestordecarreiras.wsgi.application"

# Lógica para escolher o banco de dados de acordo com o ambiente
# if os.getenv('DJANGO_ENV') == 'production':
#     DATABASES = {
#         'default': dj_database_url.parse(os.getenv("DATABASE_URL", ""))
#     }
# else:
#     # Banco de dados local (SQLite)
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#postgresql://procarreiras_user:2gfFlMXaAWYD5Ke4faqwL4WRJam49uBL@dpg-cqv814jtq21c73a3acgg-a.oregon-postgres.render.com/procarreiras
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'futurobr',
        'USER':'blackvush',
        'PASSWORD':'150220',
        'HOST':'localhost',
        'PORT':'5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'GPC','static'), 
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

STATIC_VERSION = '2.0.1'
# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# criação da pasta media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# SESSION_COOKIE_AGE = tempo de sessao dos usuarios logados


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}