"""
Django settings for backend_web_ventas project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os


# BASE_DIR es la ruta base del proyecto (la carpeta principal que contiene todos los archivos del proyecto).
BASE_DIR = Path(__file__).resolve().parent.parent


# URL que se utiliza para manejar archivos de medios cargados por los usuarios.
MEDIA_URL = '/media/'


# Ruta en el sistema de archivos donde se almacenarán los archivos de medios, en este casom en una carpeta llamada media en la carpeta base
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# La clave secreta se utiliza para criptografía en Django.
SECRET_KEY = 'django-insecure-t&@-*p_j@v7sqq!hrp#r%bqhva_ia#-4=ajzmhfl4)9n3my3c5'


# SECURITY WARNING: don't run with debug turned on in production!
# Cuando DEBUG está en True, se muestran mensajes detallados de error. Debe estar en False en producción para mayor seguridad.
DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True

# Lista de dominios o direcciones IP permitidos para servir la aplicación.
ALLOWED_HOSTS = []


# Application definition
DJANGO_BASE_APPS = [
    # Django Base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # EXTENSION
    'django_extensions',
]

REST_FRAMEWORK_APPS = [    
    # Rest_Framework
    'rest_framework',
    'rest_framework.authtoken',
]

THIRD_APPS = [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'drf_yasg',
    'corsheaders',
]

OWN_APPS = [
    #Apps
    'users',
    'main',
    'products',
    'services',
    'favorites',  

]

INSTALLED_APPS = DJANGO_BASE_APPS + REST_FRAMEWORK_APPS + THIRD_APPS + OWN_APPS 


# Identificador único para el sitio cuando se usa el framework `django.contrib.sites`.
SITE_ID = 1


# Lista de middlewares() utilizados por Django para procesar las solicitudes y respuestas HTTP.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware',


]


# Configuración específica para proveedores de autenticación social.
###### GOOGLE ######
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Allauth settings 


# Habilita el requisito para pedir un email al registrarse
ACCOUNT_EMAIL_REQUIRED = True


# Deshabilita el requisito para pedir un nombre de usuario al registrarse
ACCOUNT_USERNAME_REQUIRED = False


# Define al email como metodo de auntenticacion principal
ACCOUNT_AUTHENTICATION_METHOD = 'email'


# Requiere que los usuarios verifiquen su dirección de correo electrónico después del registro.
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


# Especifica formularios personalizados para el inicio de sesión y registro.
# El formulario de registro está definido en `users.forms.CustomSignupForm`.
ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'users.forms.CustomSignupForm'
}


# Configuración del backend de correo electrónico.
# Actualmente, se usa la consola para enviar correos electrónicos (útil para desarrollo).
#----------      CAMBIAR EN PRODUCCIÓN     
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#----------


# Se redirige a '/api/main/homelog' después del login.
LOGIN_REDIRECT_URL = '/api/main/homelog'


# Se utilizará un modelo de usuario personalizado llamado `CustomUser` que está en la aplicación `users`.
AUTH_USER_MODEL = 'users.CustomUser'


# Configuración del framework Django REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer', 
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    # Paginacion, devuelve 10 productos por defecto
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}


# Habilita la cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache', # Cache en memoria
    }
}


# Este archivo especifica las rutas principales para el enrutamiento de la aplicación.
ROOT_URLCONF = 'backend_web_ventas.urls'


########## Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['products/ztemplates',
                 'services/ztemplates',
                 'users/ztemplates',
                 'users/ztemplates/account',
                 'main/ztemplates'
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


# Backends de autenticación
# El primero es el backend predeterminado de Django, que autentica contra el modelo de usuario estándar.
# El segundo es el backend de autenticación de Allauth, que maneja el inicio de sesión a través de cuentas sociales y otros métodos proporcionados por Allauth.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Servidor WSGI
WSGI_APPLICATION = 'backend_web_ventas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
# Estos validadores se utilizan para garantizar que las contraseñas cumplan con ciertos criterios de seguridad.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Similar a otros atributos, como username
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # El minimo de caracteres
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Muy Comun
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Solo Numerica
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Panama'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Tipo de campo predeterminado para las claves primarias en los modelos.
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
