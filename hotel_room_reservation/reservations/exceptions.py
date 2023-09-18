"""
exceptions file hold exception classes for the app
"""
from hotel_room_reservation.common.exceptions import CommonException


class ReservationAlreadyExistsException(CommonException):
    """
    Custom exception class for multiple overlapping
    bookings
    """
