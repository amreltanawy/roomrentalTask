"""
Room Viewset
"""
import datetime

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from hotel_room_reservation.rooms.exceptions import RoomInactiveException
from .exceptions import ReservationAlreadyExistsException
from .models import Room, Reservation
from .serializers import ReservationSerializer
from .services import create_reservation, get_all_reservations_client, get_all_reservations_staff, cancel_reservation, \
    get_reservations_in_date_range_staff, get_reservations_in_date_range_client


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer

    def get_permissions(self):
        """
        permission for access control
        :return:
        """
        if self.action in ("retrieve", "create", "list", "cancel"):
            _permissions = [permissions.IsAuthenticated]
        elif self.action in ("update", "delete"):
            if (self.request.user.is_staff
                or self.request.user.is_admin
            ):
                _permissions = [permissions.IsAuthenticated]
            else:
                _permissions = [permissions.IsAdminUser]
        else:
            _permissions = [permissions.IsAdminUser]
        return [permission() for permission in _permissions]

    def get_queryset(self):
        """
        get specific subset of data based on user
        :return:
        """
        if self.action in ("retrieve", "list", "cancel", "update", "reservation_schedule"):
            if self.request.user.is_staff or self.request.user.is_admin:
                return get_all_reservations_staff()
            else:
                return get_all_reservations_client(user=self.request.user)
        else:
            return Reservation.objects.none()

    def create(self, request, *args, **kwargs):
        """
        create new reservation
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                create_reservation(**serializer.validated_data)
            except (ReservationAlreadyExistsException,
                    RoomInactiveException) as exception:
                return Response(status=exception.status_code, data=exception.to_dict())
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @action(detail=True, methods=["put"])
    def cancel(self, request, *args, **kwargs):
        """
        Cancel reservation controller
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pk = kwargs.get("pk")
        instance = self.get_queryset().filter(pk=pk).first()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "reservation does not exist"})
        serializer = self.serializer_class(instance=instance, data=request.data)
        if serializer.is_valid():
            cancel_reservation(reservation=instance,status=serializer.validated_data["status"])
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @action(methods=["get"],
            url_path='reservation_schedule/(?P<start_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/'
                     '(?P<end_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/')
    def reservation_schedule(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        start_date_str = kwargs.get("start_date")
        end_date_str = kwargs.get("end_date")
        date_format = "%y-%m-%d"
        start_date = datetime.datetime.strptime(start_date_str, date_format)
        end_date = datetime.datetime.strptime(end_date_str, date_format)
        if self.request.user.is_staff or self.request.user.is_admin:
            reservations = get_reservations_in_date_range_staff(
                start_date=start_date, end_date=end_date)
        else:
            reservations = get_reservations_in_date_range_client(
                user=self.request.user, start_date=start_date, end_date=end_date
            )

        paginated_data = self.paginate_queryset(reservations)
        serializer = self.serializer_class(instance=paginated_data, many=True)
        return self.get_paginated_response(serializer.data)
