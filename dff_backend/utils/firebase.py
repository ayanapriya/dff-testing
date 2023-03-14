
import os
from datetime import datetime
import logging

from django.conf import settings
from django.utils import timezone
from rest_framework import authentication

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import storage

from dff_backend.exceptions.firebase import FirebaseError
from dff_backend.exceptions.firebase import InvalidAuthToken
from dff_backend.exceptions.firebase import NoAuthToken

from dff_backend.constants import firebase_credential, firebase_storage_bucket
from dff_backend.models.user import User

log = logging.getLogger('api_log')

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credential)
    firebase_admin.initialize_app(cred,
                                  {'storageBucket': firebase_storage_bucket}
                                  )
    default_app = firebase_admin.initialize_app(cred, name='my_app')
    log.info('initialized firebase app')


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None
        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()
        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            raise InvalidAuthToken("Invalid User")

        return (user, None)


bucket_storage = storage.bucket()


def upload_to_firebase(folder_name, file):
    path = folder_name +\
        str(int(datetime.timestamp(datetime.now())))+file.name
    destination_file = bucket_storage.blob(path)
    destination_file.upload_from_file(file,
                                      content_type=file.content_type)
    destination_file.make_public()
    url = destination_file.public_url
    return {'url': url, 'path': path}


def delete_from_firebase(path):
    firebase_file = bucket_storage.blob(path)
    firebase_file.delete()


def delete_user_from_firebase(uid):
    try:
        auth.delete_user(uid)
    except Exception as e:
        log.error("user"+e.default_message)
