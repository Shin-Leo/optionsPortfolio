from django.db import models
from django.db.models import DateTimeField, JSONField
from django.contrib.auth.models import User
import json



class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    strategies = JSONField()

    def return_owner(self):
        owner = {"owner": self.user}
        return owner


class ButterflySpread(models.Model):
    id = models.BigAutoField(primary_key=True)
    lower_bound_strike = models.PositiveIntegerField()
    midpoint_strike = models.PositiveIntegerField()
    upper_bound_strike = models.PositiveIntegerField()
    low_strike_contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    mid_strike_contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_strike_contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    strategy_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = DateTimeField()
    expiry_date = DateTimeField()
    num_contracts = models.PositiveIntegerField()
    ticker = models.CharField(max_length=5)
    collapsible_tag = models.CharField(max_length=90)
    strategy_name = models.CharField(max_length=50)

    def return_attributes(self):
        attributes = {"id": self.id, "lower_strike": self.lower_bound_strike, "midpoint_strike": self.midpoint_strike,
                      "upper_strike": self.upper_bound_strike, "low_strike_contract_price": self.low_strike_contract_price,
                      "mid_strike_contract_price": self.mid_strike_contract_price,
                      "high_strike_contract_price": self.high_strike_contract_price,"strategy_price": self.strategy_price,
                      'purchase_date': self.purchase_date, "expiry_date": self.expiry_date,
                      "num_contracts": self.num_contracts,
                      "collapsible_tag": self.collapsible_tag,
                      "ticker": self.ticker, "strategy": self.strategy_name}
        return attributes

    def return_low_leg(self):
        attributes = {"lower_strike": self.lower_bound_strike,
                      "low_strike_contract_price": self.low_strike_contract_price,
                      'purchase_date': self.purchase_date, "expiry_date": self.expiry_date,
                      "contract_size": self.num_contracts, "ticker": self.ticker
                      }
        return attributes

    def return_middle_leg(self):
        attributes = {"midpoint_strike": self.midpoint_strike,
                      "mid_strike_contract_price": self.mid_strike_contract_price,
                      'purchase_date': self.purchase_date, "expiry_date": self.expiry_date,
                      "contract_size": self.num_contracts, "ticker": self.ticker
                      }
        return attributes

    def return_high_leg(self):
        attributes = {"upper_strike": self.upper_bound_strike,
                      "high_strike_contract_price": self.high_strike_contract_price,
                      'purchase_date': self.purchase_date, "expiry_date": self.expiry_date,
                      "contract_size": self.num_contracts, "ticker": self.ticker
                      }
        return attributes

    def return_collapsible_tag(self):
        return self.collapsible_tag
