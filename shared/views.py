from django.shortcuts import render

from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Settings, ContactUs, Category, Brand
from .serializers import SettingsSerializer,ContactUsSerializer, CategorySerializer, BrandSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True # Admin users have full access
        return request.method in ['GET', 'HEAD', 'OPTIONS' ] # Others have read-only access

class SettingsAdminListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer   
    
class SettingsAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    
class SettingsUserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    
class ContactUsAdminListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer   
    
class ContactUsAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    
class ContactUsUserListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly ]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    
class CategoryAdminListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   
    
class CategoryAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryUserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class BrandAdminListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer 
    
class BrandAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class BrandUserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer