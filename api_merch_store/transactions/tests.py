from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Product, Transaction, CoinTransaction
from decimal import Decimal


class TransactionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.product = Product.objects.create(type='Sword', quantity=10)

    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            user_profile=self.user_profile,
            product=self.product,
            price=Decimal('99.99')
        )
        self.assertEqual(transaction.user_profile, self.user_profile)
        self.assertEqual(transaction.product, self.product)
        self.assertEqual(transaction.price, Decimal('99.99'))
        self.assertIsNotNone(transaction.timestamp)


class CoinTransactionTestCase(TestCase):
    def setUp(self):
        self.sender_user = User.objects.create(username='sender')
        self.receiver_user = User.objects.create(username='receiver')
        self.sender_profile = UserProfile.objects.create(user=self.sender_user)
        self.receiver_profile = UserProfile.objects.create(user=self.receiver_user)

    def test_create_coin_transaction(self):
        coin_transaction = CoinTransaction.objects.create(
            sender=self.sender_profile,
            receiver=self.receiver_profile,
            amount=Decimal('20.00')
        )
        self.assertEqual(coin_transaction.sender, self.sender_profile)
        self.assertEqual(coin_transaction.receiver, self.receiver_profile)
        self.assertEqual(coin_transaction.amount, Decimal('20.00'))
        self.assertIsNotNone(coin_transaction.timestamp)

