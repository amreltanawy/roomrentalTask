from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Room
from ..common.test_helper import CommonTestHelper


class RoomTypeListViewTestCase(TestCase):
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

    def test_list_rooms_as_staff(self):

        self.authenticate_as(user=self.staff)
        # Call the list endpoint as staff
        response = self.client.get('/rooms/')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the same count
        self.assertEqual(response.data["count"], 1)

    def test_list_rooms_as_client(self):
        # Create an inactive room so it doesnt show up
        extra_room_inactive = CommonTestHelper.setup_a_new_room(status=Room.inactive)

        # Call the list endpoint as a regular client
        response = self.client.get('/rooms/')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the expected data
        self.assertEqual(response.data["count"], 1)

    def test_create_room_as_staff(self):
        # Create a new room
        self.authenticate_as(user=self.staff)
        new_room_data = {'name': 'New Room',
                         'description': 'hello this is description',
                         'capacity': 3,
                         'status': Room.active,
                         'price_per_night': 100}
        response = self.client.post('/rooms/', new_room_data, format='json')
        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the room was created in the database
        created_room = Room.objects.get(name='New Room')
        self.assertEqual(created_room.capacity, 3)

    def test_create_room_as_client(self):
        # create a new room as a regular client
        new_room_data = {'name': 'New Room',
                         'description': 'hello this is description',
                         'capacity': 3,
                         'status': Room.active,
                         'price_per_night': 100}
        self.authenticate_as(user=self.user)
        response = self.client.post('/rooms/', new_room_data, format='json')

        # Check if the response status code is 403 Forbidden (client should not have permission)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
