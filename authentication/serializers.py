from rest_framework import serializers

from authentication.models import User

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
            
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class EmailSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=555)
    
    class Meta:
        fields = ['token']

