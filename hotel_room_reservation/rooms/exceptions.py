"""
Exceptions module to handle Room Exceptions
"""
from hotel_room_reservation.common.exceptions import CommonException


class RoomInactiveException(CommonException):
    """
    Custom exception class for Inactive room
    operations
    bookings
    """
