from django.urls import path

from user_stats.views import ExpenseCategoryView, IncomeCategoryView, TotalExpenseAmountView, TotalIncomeAmountView


urlpatterns = [
    path('expense-by-category', ExpenseCategoryView.as_view(), name='expense-by-category'),
    path('income-by-category', IncomeCategoryView.as_view(), name='income-by-category'),
    path('total-expense', TotalExpenseAmountView.as_view(), name='total-expense'),
    path('total-income', TotalIncomeAmountView.as_view(), name='total-income'),
]
