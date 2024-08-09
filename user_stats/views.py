from datetime import datetime
from rest_framework import views, status, response, permissions

from django.utils import timezone

from categories.models import Category
from transactions.models import Transaction


class TransactionByCategoryView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_amount_of_transactions_by_category(self, category, transactions):
            amount = sum([transaction.amount for transaction in transactions if transaction.category == category])
            return amount
        
    def get_categories_by_user_and_type(self, user, type):
            categories = Category.objects.filter(user=user, type=type).all()
            return categories
    
    def get_dict_with_categories_and_amounts(self, categories, transactions):
            data = {}
            for category in categories:
                data[category.name] = {"amount": self.get_amount_of_transactions_by_category(category, transactions)}
            return data
    
    def get_start_and_end_date(self, request):
            start_date = request.query_params.get("start_date")
            end_date = request.query_params.get("end_date")
            try:
                if start_date and end_date:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d")
                    end_date = datetime.strptime(end_date, "%Y-%m-%d")
                    
                    tz = timezone.get_current_timezone()
                    start_date = start_date.replace(tzinfo=tz)
                    end_date = end_date.replace(tzinfo=tz)
                else:
                    return None, None
            except ValueError as e:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")

            return start_date, end_date
    

class ExpenseCategoryView(TransactionByCategoryView):
                   
        def get(self, request):
            categories = self.get_categories_by_user_and_type(request.user, "expense")
            try:
                start_date, end_date = self.get_start_and_end_date(request)
            except ValueError as e:
                return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            if start_date and end_date:
                expenses = Transaction.objects.filter(
                    user=request.user, 
                    category__in=categories, 
                    created_at__gte=start_date,
                    created_at__lte=end_date
                    ).all()
            else:
                expenses = Transaction.objects.filter(user=request.user, category__in=categories).all()
            data = self.get_dict_with_categories_and_amounts(categories, expenses)
            return response.Response({"expense_category_data": data}, status=status.HTTP_200_OK)
        

class IncomeCategoryView(TransactionByCategoryView):
                   
        def get(self, request):
            categories = self.get_categories_by_user_and_type(request.user, "income")
            
            try:
                start_date, end_date = self.get_start_and_end_date(request)
            except ValueError as e:
                return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            if start_date and end_date:
                incomes = Transaction.objects.filter(
                    user=request.user, 
                    category__in=categories, 
                    created_at__gte=start_date,
                    created_at__lte=end_date
                    ).all()
            else:
                incomes = Transaction.objects.filter(user=request.user, category__in=categories).all()
            data = self.get_dict_with_categories_and_amounts(categories, incomes)
            return response.Response({"income_category_data": data}, status=status.HTTP_200_OK)   


class TotalTransactionAmountView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_total_amount_of_transactions(self, transactions):
            total_amount = sum([transaction.amount for transaction in transactions])
            return total_amount
    
class TotalExpenseAmountView(TotalTransactionAmountView):
                   
        def get(self, request):
            expenses = Transaction.objects.filter(user=request.user, type="expense").all()
            total_expense_amount = self.get_total_amount_of_transactions(expenses)
            return response.Response({"total_expense_amount": total_expense_amount}, status=status.HTTP_200_OK)
        
class TotalIncomeAmountView(TotalTransactionAmountView):
                   
        def get(self, request):
            incomes = Transaction.objects.filter(user=request.user, type="income").all()
            total_income_amount = self.get_total_amount_of_transactions(incomes)
            return response.Response({"total_income_amount": total_income_amount}, status=status.HTTP_200_OK)
        