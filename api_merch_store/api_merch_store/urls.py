"""
URL configuration for api_merch_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import RegisterUserAPIView, UserProfileAPIView
from transactions.views import BuyProductView, SendCoinView
from products_merch.views import ProductAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/all_merch/', ProductAPIList.as_view(), name='all_merch'),
    path('api/info/', UserProfileAPIView.as_view(), name='profile'),
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/register/', RegisterUserAPIView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/buy/<str:item>/', BuyProductView.as_view(), name='buy-product'),
    path('api/sendCoin/', SendCoinView.as_view(), name='sendCoin')
]