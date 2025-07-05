from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# Inherit Django storages
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    default_acl = 'public-read'  # Make static files publicly accessible


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    default_acl = 'public-read'  # You can set to 'private' if you prefer
    file_overwrite = False  # Prevent overwriting files with the same name