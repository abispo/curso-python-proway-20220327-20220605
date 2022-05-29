from django.db import models

from financial_account.models import FinancialAccount


class Transactions(models.Model):
    debit_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, related_name='debit_account')
    credit_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, related_name='credit_account')
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_transactions"
