from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
import json
from .serializers import RegisterSerializer, UserProfileSerializer
from .models import UserProfile
from .permissons import IsAuthenticated


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            user = User.objects.get(username=response.data["username"])
            profile = UserProfile.objects.create(user=user, inventory="{}")
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "balance": profile.balance,
                "inventory": json.loads(profile.inventory),
                "coinHistory": json.loads(profile.coinHistory)
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Неверный запрос."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Внутренняя ошибка сервера."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        try:
            if not self.request.user.is_authenticated:
                return Response({"error": "Неавторизован."}, status=status.HTTP_401_UNAUTHORIZED)
            return UserProfile.objects.get(user=self.request.user)
        except UserProfile.DoesNotExist:
            return Response({"error": "Неверный запрос."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Внутренняя ошибка сервера."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
