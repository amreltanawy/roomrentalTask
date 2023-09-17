"""
Room serializer to handle data serialization into json
Also Known as Marshaling
"""
from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
