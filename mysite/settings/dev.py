"""Development settings and globals."""


from .common import *



########## DEBUG CONFIGURATION
DEBUG = False

########## END DEBUG CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
########## END CACHE CONFIGURATION





