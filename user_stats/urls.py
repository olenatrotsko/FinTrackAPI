from django.urls import path

from user_stats.views import ExpenseCategoryView, IncomeCategoryView


urlpatterns = [
    path('expense-category', ExpenseCategoryView.as_view(), name='expense-category'),
    path('income-category', IncomeCategoryView.as_view(), name='income-category'),
]