from rest_framework import serializers

from accounts.models import Account

class BaseAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'currency', 'balance', 'is_main']
        read_only_fields = ['id']

    def validate_name(self, name):
        user = self.context['request'].user
        if Account.objects.filter(user=user, name=name).exists():
            raise serializers.ValidationError('Account with this name already exists')
        return name


class CreateAccountSerializer(BaseAccountSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'currency', 'balance', 'is_main']

    def validate(self, attrs):
        attrs = super().validate(attrs)

        user = self.context['request'].user
        is_main = attrs.get('is_main')

        attrs['user'] = user

        main_account = Account.objects.filter(user=user, is_main=True).first()
        if main_account and is_main:
            raise serializers.ValidationError('Main account already exists')

        number_of_accounts = Account.objects.filter(user=user).count()
        if number_of_accounts == 0 and not is_main:
            raise serializers.ValidationError('First account must be main account')

        return attrs
    

class UpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'currency', 'balance', 'is_main']
        read_only_fields = ['is_main']
