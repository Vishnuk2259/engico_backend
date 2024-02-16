from django.urls import path
from .views import ProductAdminListCreate, ProductAdminRetrieveUpdateDestroy, ProductUserList

urlpatterns = [
    path('admin/', ProductAdminListCreate.as_view(), name = 'product-admin-list'),
    path('admin/<int:pk>/', ProductAdminRetrieveUpdateDestroy.as_view(), name = 'product-admin-detail'),
    path('',ProductUserList.as_view(), name = 'product-list')
]
