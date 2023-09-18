"""
Room Viewset
"""
from rest_framework import viewsets, permissions
from .models import Room
from .serializers import RoomSerializer
from .services import list_rooms_staff, list_rooms_client


class RoomTypeListView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_permissions(self):
        """
        permission for access control
        :return:
        """
        if self.action in ("retrieve", "list"):
            _permissions = [permissions.IsAuthenticated]
        elif self.action in ("create", "update", "delete"):
            if (self.request.user.is_staff
                or self.request.user.is_superuser
            ):
                _permissions = [permissions.IsAuthenticated]
            else:
                _permissions = [permissions.IsAdminUser]
        else:
            _permissions = [permissions.IsAdminUser]
        return [permission() for permission in _permissions]

    def get_queryset(self):
        """
        selectively get queryset based
        on user type
        :return:
        """
        if self.action in ("retrieve", "list"):
            if (self.request.user.is_staff
                or self.request.user.is_superuser
            ):
                return list_rooms_staff()
            return list_rooms_client()
        if self.action in ("create", "update", "delete"):
            return list_rooms_staff()
        return Room.objects.none()
