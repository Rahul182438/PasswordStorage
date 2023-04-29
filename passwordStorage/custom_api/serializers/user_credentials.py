import hmac
import hashlib
from rest_framework import serializers, exceptions
from django.conf import settings
from custom_api.helper.password_helpers import *
from cryptography.fernet import Fernet
from user.models import WebsiteCredentials


class UserCredentialsSerializer(serializers.Serializer):

    app_name = serializers.CharField()
    password = serializers.CharField()
    username =  serializers.CharField()

    def validate(self, attrs):

        attrs =  super().validate(attrs)
        attrs['password'] = encrypt(attrs['password'])
        return attrs

    
    def save(self, validated_data,request):

        cred = WebsiteCredentials.objects.create(
            user=request.user,
            app_name=validated_data['app_name'],
            password=validated_data['password'],
            username=validated_data['username']
        )

        cred.save()



class UserCredentialsListingSerializer(serializers.Serializer):
    
    user = serializers.CharField()
    app_name = serializers.CharField()
    password = serializers.CharField()
    username =  serializers.CharField()

