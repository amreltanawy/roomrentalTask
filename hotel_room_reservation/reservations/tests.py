"""
Reservations test
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from hotel_room_reservation.common.test_helper import CommonTestHelper
from hotel_room_reservation.reservations.models import Reservation


class ReservationViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.room = CommonTestHelper.setup_a_new_room()
        self.user = CommonTestHelper.setup_a_user(1)
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        self.staff = CommonTestHelper.setup_a_user(0)
        self.staff.is_staff = True
        self.staff.save()

    def authenticate_as(self, user):
        token = Token.objects.filter(user=user).first()
        if token is None:
            token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

    def test_create_reservation(self):
        reservation_data = {
            "user": self.user.id,
            "room": self.room.pk,  # Replace with a valid room ID
            "check_in_date": "2023-09-20",
            "check_out_date": "2023-09-25",
            "reservation_price": 0,
        }
        self.authenticate_as(user=self.user)
        response = self.client.post("/reservations/", reservation_data, format="json")
        # Check if the reservation was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(response.data["reservation_price"], "500.00")

    def test_cancel_reservation(self):
        # create a reservation
        reservation = CommonTestHelper.setup_a_new_reservation(user=self.user, room=self.room)
        reservation_id = reservation.id

        cancellation_data = {
            "status": Reservation.inactive
        }

        self.authenticate_as(user=self.staff)
        response = self.client.put(f"/reservations/{reservation_id}/cancel/", cancellation_data, format="json")
        # Check if the reservation was canceled successfully
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], Reservation.inactive)

    def test_reservation_schedule(self):
        # start_date and end_date for the schedule
        reservation = CommonTestHelper.setup_a_new_reservation(
            user=self.user, room=self.room, check_in_date="2023-09-01", check_out_date="2023-09-25"
            )
        reservation2 = CommonTestHelper.setup_a_new_reservation(
            user=self.staff, room=self.room, check_in_date="2023-08-01", check_out_date="2023-08-25"
        )
        not_counted_reservation = CommonTestHelper.setup_a_new_reservation(
            user=self.user, room=self.room, check_in_date="2022-01-01", check_out_date="2022-02-01"
        )
        start_date = "2022-09-01"
        end_date = "2024-09-01"

        self.authenticate_as(user=self.staff)
        response = self.client.get(f"/reservations/schedule/{start_date}/{end_date}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
