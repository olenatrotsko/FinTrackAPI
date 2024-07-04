from django.urls import path

from transactions.views import TransactionListCreateAPIView, TransactionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', TransactionListCreateAPIView.as_view(), name='transactions'),
    path('<int:pk>/', TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction'),
]
