from django.urls import path
from .views import (
    UserRegistrationAPIView,
    LoginAPIView,
    RefreshTokenAPIView,
    LogoutAPIView
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('token/refresh/', RefreshTokenAPIView.as_view(), name='token-refresh'),
    path('logout/', LogoutAPIView.as_view(), name='user-logout'),
]