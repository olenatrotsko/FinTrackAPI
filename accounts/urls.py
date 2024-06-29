from django.urls import path

from accounts.views import ListAccountsView, AccountDetailView

urlpatterns = [
    path('', ListAccountsView.as_view(), name='accounts'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account'),
    
]
