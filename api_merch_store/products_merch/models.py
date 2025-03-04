from django.db import models
# , connection
# from django.conf import settings
# import os, json


class Product(models.Model):
    type = models.CharField(max_length=31)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.type

    # @classmethod
    # def load_from_json(cls, file_name="products_merch/products.json"):
    #     file_path = os.path.join(settings.BASE_DIR, file_name)
    #     with open(file_path, encoding="utf-8") as f:
    #         data = json.load(f)
    #
    #     with connection.cursor() as cursor:
    #         cursor.execute(f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE;")
    #
    #     for item in data.get("merch", []):
    #         product, created = cls.objects.get_or_create(
    #             type=item["type"],
    #             defaults={"quantity": item["quantity"]}
    #         )
    #         if not created:
    #             product.quantity = item["quantity"]
    #             product.save()
