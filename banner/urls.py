from django.urls import path
from .views import BannerAdminListCreate, BannerAdminRetrieveUpdateDestroy, BannerUserList

urlpatterns = [
    path('admin/', BannerAdminListCreate.as_view(), name = 'banner-admin-list'),
    path('admin/<int:pk>/', BannerAdminRetrieveUpdateDestroy.as_view(), name = 'banner-admin-detail'),
    path('', BannerUserList.as_view(), name = 'banner-list')
]
