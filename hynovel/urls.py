"""hynovel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework.authtoken import views as drft
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from novels import views
from novels.views import AllNovelListViewSet
from useropeate.views import UserCollectionNovelViewSet

router = DefaultRouter()

router.register(r'all', AllNovelListViewSet, base_name='all_novel')
router.register(r'collect', UserCollectionNovelViewSet, base_name='collect')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', drft.obtain_auth_token),
    path('login/', obtain_jwt_token, name='login-api'),
    path('novel/', include('novels.urls')),
    # path('user/', include('django.contrib.auth.urls')),
    path('user/', include('users.urls')),
]
