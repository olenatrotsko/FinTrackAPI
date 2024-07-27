from rest_framework import views, status, response, permissions

from categories.models import Category
from transactions.models import Transaction

class TransactionCategoryView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_amount_of_transactions_by_category(self, category, transactions):
            amount = 0.0
            for transaction in transactions:
                if transaction.category == category:
                    amount += transaction.amount
            return amount
        
    def get_categories_by_user_and_type(self, user, type):
            categories = Category.objects.filter(user=user, type=type).all()
            return categories
    
    def get_dict_with_categories_and_amounts(self, categories, transactions):
            data = {}
            for category in categories:
                data[category.name] = {"amount": self.get_amount_of_transactions_by_category(category, transactions)}
            return data
    

class ExpenseCategoryView(TransactionCategoryView):
                   
        def get(self, request):
            categories = self.get_categories_by_user_and_type(request.user, "expense")
            expenses = Transaction.objects.filter(user=request.user, category__in=categories).all()
            data = self.get_dict_with_categories_and_amounts(categories, expenses)
            return response.Response({"expense_category_data": data}, status=status.HTTP_200_OK)
        

class IncomeCategoryView(TransactionCategoryView):
                   
        def get(self, request):
            categories = self.get_categories_by_user_and_type(request.user, "income")
            incomes = Transaction.objects.filter(user=request.user, category__in=categories).all()
            data = self.get_dict_with_categories_and_amounts(categories, incomes)
            return response.Response({"income_category_data": data}, status=status.HTTP_200_OK)   
