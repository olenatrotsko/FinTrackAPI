from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import RegisterView, VerifyEmail, LoginView, PasswordTokenCheckAPIView, RequestPasswordResetEmail


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('request-password-reset/', RequestPasswordResetEmail.as_view(), name='request-password-reset'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='password-reset'),
]
