from django.contrib import admin
from .models import Tools

@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'content', 'file', 'file_type', 'created_at', 'updated_at')
    search_fields = ('tool_name', 'file_type')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('tool_name', 'file_type', 'created_at', 'updated_at')
    ordering = ('-created_at',)
