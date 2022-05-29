from django.db import models

from users.models import User


class FinancialAccount(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField(default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tb_financial_accounts'
