from django.db import models
from hotel_room_reservation.users.models import User
from hotel_room_reservation.rooms.models import Room


class Reservation(models.Model):
    """
    room reservation model
    """
    active = 1
    inactive = 2

    STATUS_TYPES = (
        (active, "Active"),
        (inactive, "Inactive"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPES, default=active, db_index=True)
    reservation_price = models.DecimalField(max_digits=100, decimal_places=2)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    meta = models.JSONField(default=dict)

    def __str__(self):
        return f"Reservation for {self.user} ({self.check_in_date} to {self.check_out_date})"
