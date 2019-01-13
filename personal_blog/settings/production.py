import django_heroku

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from .local import *
except ImportError:
    pass

# Allow all host headers
ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '0.0.0.0'
]

# Configure Django App for Heroku.
django_heroku.settings(locals())

# AWS settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

STATICFILES_STORAGE = 'personal_blog.custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'personal_blog.custom_storages.MediaStorage'

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

AWS_DEFAULT_ACL = None
