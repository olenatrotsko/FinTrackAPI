from django.db import models

from authentication.models import User

class Category(models.Model):

    CATEGORY_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense')
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    type = models.CharField(max_length=8, choices=CATEGORY_TYPES, blank=False, null=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    