from django.shortcuts import render

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True # Admin users have full access
        return request.method in ['GET', 'HEAD', 'OPTIONS' ] # Others have read-only access

class ProductAdminListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUserList(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer