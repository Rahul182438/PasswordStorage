import re
import requests
import json
from urllib import request
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.conf import settings
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
)
from user.models import WebsiteCredentials
from custom_api.serializers.user_credentials import UserCredentialsSerializer
from custom_api.helper.response_helpers import success_response, error_response
from custom_api.helper.password_helpers import generate_password, decrypt
from custom_api.helper.database_helpers import get_or_none


class StoreCredentialsView(viewsets.ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        serializer = UserCredentialsSerializer(data=request.data,context={"request":request})

        if not serializer.is_valid():
            return error_response(status=HTTP_400_BAD_REQUEST, msg="error occured", data=serializer.errors)

        serializer.save(serializer.validated_data,request)
        return success_response(status=HTTP_200_OK,
                                msg=f"API to insert user credentials",
                                data=serializer.data)

    def get_random_password(self, request):

        try:
            password = generate_password(13)
            return success_response(status=HTTP_200_OK,
                                    msg=f"Password generated",
                                    data=password)

        except Exception as error:
            password = None
            return error_response(status=HTTP_400_BAD_REQUEST, msg="Password generation error", data={"error":str(error)})



class ListCredentialsView(viewsets.ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
 
        website_credentials_obj = WebsiteCredentials.objects.filter(user=request.user)
        print("🐍 File: views/generatePassword.py | Line: 65 | get ~ website_credentials_obj",website_credentials_obj)

        result = []
        for items in website_credentials_obj:
            item_dict = {}
            item_dict['app_name'] = items.app_name
            item_dict['password'] = decrypt(items.password)
            item_dict['username'] = items.username
            result.append(item_dict)

        return success_response(status=HTTP_200_OK,
                                msg=f"API to fetch user credentials",
                                data=result)

