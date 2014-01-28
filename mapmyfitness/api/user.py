from .base import BaseAPI
from ..validators.user import UserValidator
from ..serializers import UserSerializer, UserProfilePhotoSerializer
from .mixins import Searchable, Findable, Updateable


class User(BaseAPI, Searchable, Findable):
    path = '/user'
    validator_class = UserValidator
    serializer_class = UserSerializer
    embedded_name = 'user'


class UserProfilePhoto(BaseAPI, Findable, Updateable):
    path = '/user_profile_photo'
    serializer_class = UserProfilePhotoSerializer
