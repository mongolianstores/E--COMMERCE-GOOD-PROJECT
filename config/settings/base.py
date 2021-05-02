
import os
import configparser
#from pathlib                           import Path
from decouple                          import config




#Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



SECRET_KEY = 'qrcnuk0u$qj&6lm*_ft&5wdo)p=s4x&f3h$6ky#qte%sn)+c)%'



DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'shop',
    'blog',
    
    
    # 3rd party app 
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django_countries',
    

    'crispy_forms',
]



LOGIN_REDIRECT_URL ='/'

ACCOUNT_LOGOUT_REDIRECT_URL = '/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]




ROOT_URLCONF = 'config.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


CONFIG_DIR = os.path.join(BASE_DIR, 'config/')

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))

DATABASES = {}



# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE       = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#Auth
AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email' # login with email 
ACCOUNT_UNIQUE_EMAIL = True


SITE_ID = 1



# STRIPE_PUBLISHABLE_KEY= 'pk_test_51I8IgYH5FGERXivQk0hNGJ6O1OiLqNez12vyz2gzqK80IjK5ujdfut2AaVttzV2FRKCzNqFyds1z6Ik5fFSbwrcW00zoTjorcD'
# STRIPE_SECRET_KEY = 'sk_test_51I8IgYH5FGERXivQRzUk4tvuIbXhfQjKDZjxu0n8yNKrKyEvwZgPGWvAvbsE7gw1cyc5JzdfAnRhSLBUVFWDum6400wGnA5iuA'

