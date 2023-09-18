"""
Reservations Services where all business logic for
reservations are located
"""
from django.db import transaction

from hotel_room_reservation.rooms.models import Room
from .exceptions import ReservationAlreadyExistsException
from .models import Reservation


def create_reservation(**reservation_data):
    with transaction.atomic():
        room = reservation_data.get('room')
        check_in_date = reservation_data.get('check_in_date')
        check_out_date = reservation_data.get('check_out_date')
        period = check_out_date - check_in_date
        reservation_price = period.days * room.price_per_night
        reservation_data["reservation_price"] = reservation_price
        # Check if there are any reservations for the same room type within the given date range
        existing_reservations = Reservation.objects.filter(
            room=room,
            status=Reservation.active,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date
        )
        if room.status == Room.inactive:
            raise Exception("Inactive room exception")

        if existing_reservations.exists():
            raise ReservationAlreadyExistsException(
                "There are existing reservations for this room "
                "in the specified date range.")

        # Create the reservation
        reservation = Reservation.objects.create(**reservation_data)
        return reservation


def cancel_reservation(reservation, status=Reservation.inactive):
    """
    :param reservation:
    :param status:
    :return:
    """
    reservation.status = status
    reservation.save()


def get_reservations_in_date_range_staff(start_date, end_date):
    return Reservation.objects.filter(check_in_date__gte=start_date, check_out_date__lte=end_date)


def get_reservations_in_date_range_client(user, start_date, end_date):
    return Reservation.objects.filter(
        user=user, check_in_date__gte=start_date, check_out_date__lte=end_date
    )


def get_all_reservations_staff():
    """
    retrieve all reservations
    :return:
    """
    return Reservation.objects.all()


def get_all_reservations_client(user):
    """
    get all reservations made by a user
    :param user:
    :return:
    """
    return Reservation.objects.filter(user=user)
