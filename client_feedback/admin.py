from django.contrib import admin
from .models import Feedback 

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'content', 'created_at', 'updated_at')
    search_fields = ('client_name',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('client_name', 'created_at', 'updated_at')
    ordering = ('-created_at',)
