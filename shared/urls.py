from django.urls import path
from . import views

urlpatterns = [
    
    path('settings/admin/', views.SettingsAdminListView.as_view(), name='settings-admin-list'),
    path('settings/admin/<int:pk>/', views.SettingsAdminDetailView.as_view(), name='settings-admin-detail'),
    path('settings/user/', views.SettingsUserListView.as_view(), name='settings-user-list'),
    
    path('contactus/admin/', views.ContactUsAdminListView.as_view(), name='contactus-admin-list'),
    path('contactus/admin/<int:pk>/', views.ContactUsAdminDetailView.as_view(), name='contactus-admin-detail'),
    path('contactus/user/', views.ContactUsUserListView.as_view(), name='contactus-user-list'),
    
    path('category/admin/', views.CategoryAdminListView.as_view(), name='category-admin-list'),
    path('category/admin/<int:pk>/', views.CategoryAdminDetailView.as_view(), name='category-admin-detail'),
    path('category/user/', views.CategoryUserListView.as_view(), name='category-user-list'),
    
    path('brand/admin/', views.BrandAdminListView.as_view(), name='brand-admin-list'),
    path('brand/admin/<int:pk>/', views.BrandAdminDetailView.as_view(), name='brand-admin-detail'),
    path('brand/user/', views.BrandUserListView.as_view(), name='brand-user-list'),

]
