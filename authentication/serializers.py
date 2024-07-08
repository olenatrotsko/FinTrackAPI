from django.contrib import auth

from rest_framework import serializers
from rest_framework import exceptions

from authentication.models import User
from authentication.utils import Util

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

   
    def validate(self, attrs):
        """
        Validates the input attributes.
        """
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
            
        if first_name == last_name:
            raise serializers.ValidationError("First name and last name must be different.")
        print(attrs)
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class EmailSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=555)
    
    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    tokens = serializers.CharField(max_length=255, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials, try again')
        
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account disabled, contact admin')
        
        if not user.is_verified:
            raise exceptions.AuthenticationFailed('Account is not verified, check your email for the verification link')
        
       
        return {
            'email': user.email,
            'tokens': user.get_tokens()
        }

class RequestResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']
    