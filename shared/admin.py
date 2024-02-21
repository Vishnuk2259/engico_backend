from django.contrib import admin
from .models import Settings, ContactUs, Category, Brand

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'submitted_at')
    search_fields = ['first_name', 'last_name', 'email', 'subject', 'comments']
    list_filter = ('submitted_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')
    search_fields = ['name']
    list_filter = ('parent',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent_brand')
    search_fields = ['name']
    list_filter = ('parent_brand',)
