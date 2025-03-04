from django.test import TestCase
from django.conf import settings
import json
import os
from products_merch.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(type="T-shirt", quantity=10)
        self.product2 = Product.objects.create(type="Hoodie", quantity=5)

    def test_str_method(self):
        self.assertEqual(str(self.product1), "T-shirt")
        self.assertEqual(str(self.product2), "Hoodie")

    def test_load_from_json(self):
        test_data = {
            "merch": [
                {"type": "T-shirt", "quantity": 20},
                {"type": "Mug", "quantity": 15}
            ]
        }
        test_file = os.path.join(settings.BASE_DIR, "test_products.json")

        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f)

        Product.load_from_json("test_products.json")

        self.assertEqual(Product.objects.get(type="T-shirt").quantity, 20)
        self.assertEqual(Product.objects.get(type="Mug").quantity, 15)

        os.remove(test_file)
