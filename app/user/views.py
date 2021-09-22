from user.serializers import UserSerializer, AuthTokenSerializer

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import filters
# from rest_framework.permissions import IsAuthenticated
#
# from profiles_api import serializers
# from profiles_api import models
# from profiles_api import permissions


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
