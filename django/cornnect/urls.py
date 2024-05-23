"""
URL configuration for cornnect project.

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
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/signup/', include('dj_rest_auth.registration.urls')),
    # path('api/auth/logout/', include('dj_rest_auth.registration.urls')),
    path('api/user/', include('accounts.urls')), # accounts 앱의 URL은 /api/user/ 경로로 연결
    path('movies/', include('movies.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # 토큰 얻기 엔드포인트
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
