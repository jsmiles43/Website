"""Development settings and globals."""


from common import *



########## DEBUG CONFIGURATION
DEBUG = True
########## END DEBUG CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'projectsdb',
		'USER': 'joe',
		'PASSWORD': '103noctil51',
		'HOST': 'localhost',
		'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
