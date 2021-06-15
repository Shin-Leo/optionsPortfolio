from django.db import models
from django.db.models import DateTimeField


class Strategy(models.Model):
    id = models.BigAutoField(primary_key=True)
    strike = models.PositiveIntegerField()
    contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = DateTimeField()
    num_contracts = models.PositiveIntegerField()
    ticker = models.CharField(max_length=5)

    class Meta:
        abstract = True


class CoveredCall(Strategy):
    strategy_name = models.CharField(max_length=20)
