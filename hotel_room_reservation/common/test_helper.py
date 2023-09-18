"""
testing helpers method
"""
from hotel_room_reservation.reservations.models import Reservation
from hotel_room_reservation.rooms.models import Room
from hotel_room_reservation.users.models import User


class CommonTestHelper:
    """
    common helper utilities
    """

    @staticmethod
    def setup_a_new_room():
        room_data = {
            "name": "Room 201",
            "description": "Standard Double Room",
            "capacity": 2,
            "price_per_night": 100,
            "meta": {},
            "status": 1
        }
        existing_room = Room.objects.first()
        if existing_room is None:
            return Room.objects.create(
                **room_data
            )
        return existing_room

    @staticmethod
    def setup_a_new_reservation(user: User,
                                room: Room,
                                check_in_date="2023-09-20",
                                check_out_date="2023-09-25"
                                ):
        reservation_data = {
            "user": user,
            "room": room,
            "status": 1,
            "reservation_price": "199.99",
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "meta": {}
        }
        existing_reservation = Reservation.objects.filter(user=user, room=room).first()
        if existing_reservation is None:
            return Reservation.objects.create(
                **reservation_data
            )
        return existing_reservation

    @staticmethod
    def setup_a_user(number_tag=1):
        email = f"email{number_tag}@test.com"
        existing_user = User.objects.filter(email=email, is_staff=False, is_superuser=False).first()
        if existing_user is None:
            return User.objects.create_user(
                email=email,
                password="testpassword"
            )
        return existing_user
