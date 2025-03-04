from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly


class ProductAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = ProductAPIListPagination
