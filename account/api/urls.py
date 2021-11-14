from django.urls import path
from .api_views import UserCreateAPIView

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name="user_create_api"),
]
