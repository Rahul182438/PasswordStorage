"""
URL configuration for passwordStorage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from custom_api.views.authentication import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('custom_api.urls'), name='api_custom'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refreshToken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
