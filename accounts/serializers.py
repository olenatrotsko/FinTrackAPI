from rest_framework import serializers

from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'currency', 'balance', 'is_main']


class CreateUpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'currency', 'balance', 'is_main']

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        name = attrs.get('name')
        is_main = attrs.get('is_main')

        name_exists = Account.objects.filter(user=user, name=name).exists()
        if name_exists:
            raise serializers.ValidationError('Account with this name already exists')
        
        main_account = Account.objects.filter(user=user, is_main=True).first()
        if is_main and main_account:
            main_account.is_main = False
            main_account.save()

        number_of_accounts = Account.objects.filter(user=user).count()
        if number_of_accounts == 0:
            attrs['is_main'] = True

        return super().validate(attrs)
    