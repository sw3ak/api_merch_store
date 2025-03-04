from django.db import models
from django.contrib.auth.models import User
import json


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    inventory = models.TextField(default="{}")
    coinHistory = models.TextField(default="{}")

    def get_inventory(self):
        return json.loads(self.inventory)

    def get_coinHistory(self):
        return json.loads(self.coinHistory)

    def set_inventory(self, inventory_dict):
        self.inventory = json.dumps(inventory_dict)
        self.save()

    def set_coinHistory(self, coinHistory_dict):
        self.coinHistory = json.dumps(coinHistory_dict)
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.balance} монет"
