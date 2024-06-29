from django.db import models

from authentication.models import User


class Account(models.Model):

    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]

    name = models.CharField(max_length=50, blank=False, null=False)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=False, null=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_main = models.BooleanField(default=False, blank=False, null=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
