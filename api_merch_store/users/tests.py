from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from decimal import Decimal


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.balance, Decimal('1000.00'))
        self.assertEqual(self.user_profile.get_inventory(), {})
        self.assertEqual(self.user_profile.get_coinHistory(), {})

    def test_set_inventory(self):
        new_inventory = {"sword": 1, "shield": 2}
        self.user_profile.set_inventory(new_inventory)
        self.assertEqual(self.user_profile.get_inventory(), new_inventory)

    def test_set_coinHistory(self):
        new_coin_history = {"transactions": ["tx1", "tx2"]}
        self.user_profile.set_coinHistory(new_coin_history)
        self.assertEqual(self.user_profile.get_coinHistory(), new_coin_history)

    def test_user_profile_str(self):
        expected_str = f"{self.user.username} - {self.user_profile.balance} монет"
        self.assertEqual(str(self.user_profile), expected_str)