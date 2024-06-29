from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import Account
from accounts.serializers import AccountSerializer, CreateUpdateAccountSerializer


class ListAccountsView(views.APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        accounts = Account.objects.filter(user=request.user).all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print(request.user)
        serializer = CreateUpdateAccountSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AccountDetailView(views.APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        account = Account.objects.filter(user=request.user, id=pk).first()
        if not account:
            return Response({'error': 'Account for this user was not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def put(self, request, pk):
        account = Account.objects.filter(user=request.user, id=pk).first()
        serializer = CreateUpdateAccountSerializer(account, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    