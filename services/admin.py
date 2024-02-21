from django.contrib import admin
from .models import BaseModel, Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'title', 'created_at', 'updated_at')
    search_fields = ('service_name', 'title', 'subtitle')
    list_filter = ('service_name',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
