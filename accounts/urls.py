from django.urls import path

from .views import *

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView






urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("logout/", UserLogoutAPTView.as_view(), name="logout"),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
    path("user-info/", UserAPIView.as_view(), name="user-info"),
    path("access-token/", TokenVerifyView.as_view(), name="access-token"),
]
