from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import RegisterView, SetNewPasswordAPIView, VerifyEmail, LoginView, PasswordTokenCheckAPIView, RequestPasswordResetEmailAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('request-password-reset/', RequestPasswordResetEmailAPIView.as_view(), name='request-password-reset'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='password-reset'),
    path('complete-password-reset/', SetNewPasswordAPIView.as_view(), name='complete-password-reset'),
]
