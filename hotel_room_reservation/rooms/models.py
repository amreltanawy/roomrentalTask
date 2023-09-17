"""
Rooms model to maintain room details
"""
from django.db import models


class Room(models.Model):
    """
    Room database model
    """
    # room statuses
    active = 1
    inactive = 2

    ROOM_STATUSES = (
        (active, "Active"),
        (inactive, "Inactive"),
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(db_index=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    meta = models.JSONField(default=dict)
    status = models.PositiveSmallIntegerField(choices=ROOM_STATUSES, db_index=True)

    def __str__(self):
        return self.name
