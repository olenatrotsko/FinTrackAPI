from django.urls import path

from transactions.views import TransactionListCreateAPIView

urlpatterns = [
    path('', TransactionListCreateAPIView.as_view(), name='transactions'),
    # path('<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
]
