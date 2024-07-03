from rest_framework import generics, permissions

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



