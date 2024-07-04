from decimal import Decimal
from rest_framework import generics, permissions

from accounts.models import Account
from transactions.models import Transaction
from transactions.permissions import IsOwner
from transactions.serializers import TransactionSerializer

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data['amount']
        type = serializer.validated_data['type']
        account = serializer.validated_data['account']

        if type == 'income':
            account.balance += amount
            account.save()

        if type == 'expense':
            account.balance -= amount
            account.save()
        
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)

        instance = self.get_object()  
        old_transaction = TransactionSerializer(instance).data
        old_amount = Decimal(old_transaction['amount'])

        amount = serializer.validated_data['amount']
        type = serializer.validated_data['type']
        account = serializer.validated_data['account']

        if type == 'income':
            account.balance -= old_amount
            account.balance += amount
            account.save()

        if type == 'expense':
            account.balance += old_amount
            account.balance -= amount
            account.save()
        
        return serializer.save(user=self.request.user)
    
    def perform_destroy(self, instance):
        old_transaction = TransactionSerializer(instance).data
        old_amount = Decimal(old_transaction['amount'])

        type = old_transaction['type']
        account_id = old_transaction['account']
        account = Account.objects.get(id=account_id)

        if type == 'income':
            account.balance -= old_amount
            account.save()

        if type == 'expense':
            account.balance += old_amount
            account.save()
        
        return instance.delete()

    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
