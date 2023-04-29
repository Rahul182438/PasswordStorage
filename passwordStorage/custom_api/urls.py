
from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from django.conf.urls.static import static
from django.conf import settings
from custom_api.views.generatePassword import *
from custom_api.views.authentication import *



urlpatterns = [
    path('store-credentials/',StoreCredentialsView.as_view({"post":"post"}),name='store-credentials'), 
    path('generate-password/',StoreCredentialsView.as_view({"get":"get_random_password"}),name='generate-password'), 
    path('list-credentials/',ListCredentialsView.as_view({"get":"get"}),name='list-credentials'), 
]
