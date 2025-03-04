from django.contrib import admin
from .models import Transaction, CoinTransaction


admin.site.register(Transaction)
admin.site.register(CoinTransaction)
