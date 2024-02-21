from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'page_url', 'banner_type', 'content', 'file', 'file_type', 'created_at', 'updated_at')
    search_fields = ('title', 'page_url', 'banner_type', 'file_type')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('banner_type', 'file_type', 'created_at', 'updated_at')
    ordering = ('-created_at',)