from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
import json


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    inventory = serializers.JSONField()

    class Meta:
        model = UserProfile
        fields = ('balance', 'inventory', 'coinHistory')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['inventory'] = json.loads(instance.inventory)
        data['coinHistory'] = json.loads(instance.coinHistory)
        return data

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.inventory = json.dumps(validated_data.get('inventory', json.loads(instance.inventory)))
        instance.coinHistory = json.dumps(validated_data.get('coinHistory', json.loads(instance.coinHistory)))
        instance.save()
        return instance
