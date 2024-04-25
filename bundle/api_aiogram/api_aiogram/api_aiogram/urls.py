"""
URL configuration for api_aiogram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from api_aiogram import settings
from vpn_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get_vpn_list/', VpnApiView.as_view(), name='VpnApiView'),
    path('api/v1/get_last_item/', GetLastItemApiView.as_view(), name='GetLastItemApiView'),
    path('api/v1/remove_last_item/', RemoveLastItemApiView.as_view(), name='RemoveLastItemApiView'),
    path('api/v1/add_user_info/', GetUserUseInfo.as_view(), name='GetUserUseInfo'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)