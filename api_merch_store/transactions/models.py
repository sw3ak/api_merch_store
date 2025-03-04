from django.contrib.auth.models import User
from django.db import models


from products_merch.models import Product
from users.models import UserProfile


class Transaction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} купил {self.product.type} за {self.price} монет"


class CoinTransaction(models.Model):
    sender = models.ForeignKey(UserProfile, related_name="sent_transactions", on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name="received_transactions", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.user.username} перевел {self.amount} монет {self.receiver.user.username}"
