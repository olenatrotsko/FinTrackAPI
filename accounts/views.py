from django.shortcuts import get_object_or_404

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import Account
from accounts.permissions import IsOwner
from accounts.serializers import BaseAccountSerializer, CreateAccountSerializer, UpdateAccountSerializer


class ListAccountsView(views.APIView):

    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        accounts = Account.objects.filter(user=request.user).all()
        serializer = BaseAccountSerializer(accounts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CreateAccountSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountDetailView(views.APIView):

    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, pk):
        account = get_object_or_404(Account, id=pk)
        serializer = BaseAccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk):
        account = get_object_or_404(Account, id=pk)
        serializer = UpdateAccountSerializer(account, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        account = get_object_or_404(Account, id=pk)

        if account.is_main:
            return Response({'error': 'Main account cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)
        
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    