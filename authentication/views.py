import os
import jwt

from django.urls import reverse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import RegisterSerializer
from authentication.models import User
from authentication.utils import Util

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        relative_link = reverse('verify-email')
        current_site = get_current_site(request).domain
        absurl = 'http://' + current_site + relative_link + "?token=" + str(token)
        email_body = 'Hi ' + user.first_name + '!\nUse the link below to verify your email \n' + absurl
        
        data = {'email_subject': 'Verify your email', 'email_body': email_body, 'to_email': user.email}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)
    

class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            