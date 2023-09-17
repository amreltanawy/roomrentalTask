"""
Services file is a centeralized location for
all business logic related to the rooms
"""
from django.db.models import QuerySet
from .models import Room


def list_rooms_staff() -> QuerySet:
    """
    returns all rooms in the system
    :return:
    """
    return Room.objects.all()


def list_rooms_client() -> QuerySet:
    """
    returns list of room accessible to the given client
    :return:
    """
    return Room.objects.filter(status=Room.active)
