"""
Reservation Serializer
"""

from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class CancelReservationSerializer(serializers.ModelSerializer):
    """
    this is a dedicated serializer for handling
    status update of the reservation
    """
    class Meta:
        model = Reservation
        fields = ["status"]
