from .settings import AWS_PUBLIC_MEDIA_LOCATION
from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    location = AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False
    default_acl = 'public-read'


    