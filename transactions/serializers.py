from rest_framework import serializers

from accounts.models import Account
from categories.models import Category
from transactions.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'type', 'description', 'created_at', 'user', 'account', 'category']
        read_only_fields = ['created_at', 'user']

    # def __init__(self, *args, **kwargs):
    #     super(TransactionSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request:
    #         user = request.user
    #         transaction_type = self.initial_data.get('type')  
    #         self.fields['account'].queryset = Account.objects.filter(user=user, type=transaction_type)
    #         self.fields['category'].queryset = Category.objects.filter(user=user, type=transaction_type)


    def validate(self, attrs):
        request = self.context['request']
        user = request.user

        amount = attrs.get('amount')
        account = attrs.get('account')
        category = attrs.get('category')
        type = attrs.get('type')

        if user != request.user:
            raise serializers.ValidationError("The user does not match the authenticated user.")

        if account.user != user:
            raise serializers.ValidationError("The account does not belong to the authenticated user.")
        
        if category.user != user:
            raise serializers.ValidationError("The category does not belong to the authenticated user.")

        if amount <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        
        if category.type != type:
            raise serializers.ValidationError("The category type does not match the transaction type.")
        
        return super().validate(attrs)
