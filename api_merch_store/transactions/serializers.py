from django.contrib.auth.models import User
from rest_framework import serializers


from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class SendCoinSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=150)
    coins = serializers.IntegerField(min_value=1)
