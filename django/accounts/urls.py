from django.urls import path
from .views import update_user

urlpatterns = [
    path('update/', update_user, name='update_user'), # /api/user/update/ 경로로 매핑
]
