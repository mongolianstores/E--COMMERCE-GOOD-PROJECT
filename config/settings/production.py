
import      dj_database_url

from        .base                          import *






DEBUG = config('DEBUG')



ALLOWED_HOSTS = ['*']




MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]



DATABASES['default'] =  dj_database_url.config()



# Honor the 'X-Forwarded-Proto' header fro request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_XFORWARDED_PROTO', 'https')







# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'



prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

