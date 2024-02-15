from django.urls import path
from .views import ServiceAdminListCreate, ServiceAdminRetrieveUpdateDestroy, ServiceUserList

urlpatterns = [
    path('admin/', ServiceAdminListCreate.as_view(), name = 'service-admin-list'),
    path('admin/<int:pk>/', ServiceAdminRetrieveUpdateDestroy.as_view(), name = 'service-admin-detail'),
    path('', ServiceUserList.as_view(), name = 'service-list')
]
