from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from products_merch.models import Product
from users.models import UserProfile
from .models import Transaction, CoinTransaction
from .serializers import TransactionSerializer, SendCoinSerializer
from .permissons import IsAuthenticated


class BuyProductView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, item):
        if not request.user.is_authenticated:
            return Response({"error": "Не авторизован."}, status=status.HTTP_401_UNAUTHORIZED)

        product = Product.objects.filter(type=item).first()
        if not product:
            return Response({"error": "Товар не найден"}, status=status.HTTP_404_NOT_FOUND)

        price = product.quantity
        user_profile = UserProfile.objects.filter(user=request.user).first()
        if user_profile.balance < price:
            return Response({"error": "Недостаточно средств"}, status=status.HTTP_400_BAD_REQUEST)

        user_profile.balance -= price
        user_profile.save()

        inventory = user_profile.get_inventory()
        inventory[item] = inventory.get(item, 0) + 1
        user_profile.set_inventory(inventory)

        transaction = Transaction.objects.create(user_profile=user_profile, product=product, price=price)
        serializer = self.get_serializer(transaction)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SendCoinView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SendCoinSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "description": "Неверный запрос."
            }, status=status.HTTP_400_BAD_REQUEST)

        sender = request.user
        receiver_username = serializer.validated_data["user"]
        coins = serializer.validated_data["coins"]

        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return Response({
                "description": "Неверный запрос."
            }, status=status.HTTP_400_BAD_REQUEST)

        if sender == receiver:
            return Response({
                "description": "Неверный запрос."
            }, status=status.HTTP_400_BAD_REQUEST)

        sender_profile = sender.userprofile
        receiver_profile = receiver.userprofile

        if sender_profile.balance < coins:
            return Response({
                "description": "Неверный запрос."
            }, status=status.HTTP_400_BAD_REQUEST)

        sender_profile.balance -= coins
        sender_history = sender_profile.get_coinHistory() or {}
        sender_history.setdefault("sent", []).append({"to": receiver.username, "amount": coins})
        sender_profile.set_coinHistory(sender_history)
        sender_profile.save()

        receiver_profile.balance += coins
        receiver_history = receiver_profile.get_coinHistory() or {}
        receiver_history.setdefault("received", []).append({"from": sender.username, "amount": coins})
        receiver_profile.set_coinHistory(receiver_history)
        receiver_profile.save()

        CoinTransaction.objects.create(sender=sender_profile, receiver=receiver_profile, amount=coins)

        return Response({
            "description": "Успешный ответ."
        }, status=status.HTTP_200_OK)
