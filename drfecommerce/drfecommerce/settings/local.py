from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aw-m(%7ey%e)20jlguv+2$y0((4)2e$i$m8pf5h)m_6w&x02-m'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME",'ecommerce'),
        'USER': os.environ.get("DB_USER",'root'),
        'PASSWORD': os.environ.get("DB_PASS",'1234'),
        'HOST': os.environ.get("DB_HOST",'127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '3306'),
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]