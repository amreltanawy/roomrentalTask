from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'reservation_price', 'status')
    list_filter = ('status',)
    search_fields = ('user', 'room')
