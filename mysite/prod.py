"""Development settings and globals."""


from common import *



########## DEBUG CONFIGURATION
DEBUG = True
########## END DEBUG CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'projectdb',
		'USER': 'joe',
		'PASSWORD': '103noctil51',
		'HOST': 'localhost',
		'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION

########## END CACHE CONFIGURATION
