from django.db import models

from accounts.models import Account
from categories.models import Category

class Transaction(models.Model):

    CATEGORY_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense')
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    type = models.CharField(max_length=8, choices=CATEGORY_TYPES, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
