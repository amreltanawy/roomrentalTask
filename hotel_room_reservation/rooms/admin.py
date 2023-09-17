from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('description', 'capacity', 'price_per_night', 'status')
    list_filter = ('status',)
    search_fields = ('description',)
