from django.shortcuts import render

from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True # Admin users have full access
        return request.method in ['GET', 'HEAD', 'OPTIONS' ] # Others have read-only access

class ServiceAdminListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceAdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ServiceUserList(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
