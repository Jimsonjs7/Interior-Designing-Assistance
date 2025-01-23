# designs/admin.py
from django.contrib import admin
from .models import Design

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'description')
    search_fields = ('name',)
    list_filter = ('name',)  # Add filters for easier navigation
    ordering = ('name',)  # Order by name alphabeticall