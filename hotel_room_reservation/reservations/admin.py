from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'price_per_night', 'status')
    list_filter = ('status',)
    search_fields = ('user', 'room')
