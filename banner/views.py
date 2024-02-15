from django.shortcuts import render

from rest_framework import generics
from .models import Banner
from .serializers import BannerSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True # Admin users have full access
        return request.method in ['GET', 'HEAD', 'OPTIONS' ] # Others have read-only access

class BannerAdminListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerAdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    
class BannerUserList(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
