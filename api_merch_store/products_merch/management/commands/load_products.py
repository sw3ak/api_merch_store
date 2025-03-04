import json
from django.core.management.base import BaseCommand
from products_merch.models import Product


class Command(BaseCommand):
    help = "Загружает продукты из JSON-файла"

    def handle(self, *args, **kwargs):
        file_path = "products_merch/products.json"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                products = [Product(type=item["type"], quantity=item["quantity"]) for item in data]
                Product.objects.bulk_create(products, ignore_conflicts=True)
                self.stdout.write(self.style.SUCCESS(f"Загружено {len(products)} продуктов"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка загрузки: {e}"))
