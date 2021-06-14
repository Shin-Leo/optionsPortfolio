from django.db import models
from django.db.models import DateTimeField


class Strategy(models.Model):
    id = models.BigAutoField(primary_key=True)
    strike = models.PositiveIntegerField(null=True)
    contract_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    expiry_date = DateTimeField(null=True)
    num_contracts = models.PositiveIntegerField(null=True)
    ticker = models.CharField(null=True, max_length=5)

    class Meta:
        abstract = True


class CoveredCall(Strategy):
    strategy_name = models.CharField(max_length=20)
