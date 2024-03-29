from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'brand', 'category', 'service', 'created_at', 'updated_at')
    search_fields = ('product_title', 'brand__name', 'category__name', 'service__name')
    list_filter = ('brand', 'category', 'service', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    
