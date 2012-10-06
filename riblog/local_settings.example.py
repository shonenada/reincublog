# Debugging flags

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_pass',
        'HOST': '',
        'PORT': '',
    }
}

# Key for storing things
# You can generate one of these on this site
# http://www.miniwebtool.com/django-secret-key-generator/

SECRET_KEY = 'foofoofoofoofoofoofoofoofoo'
