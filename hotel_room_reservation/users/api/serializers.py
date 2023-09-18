from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from hotel_room_reservation.users.models import User as UserType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(
        max_length=255, required=True, allow_null=True, allow_blank=True
    )
    last_name = serializers.CharField(
        max_length=255, required=False, allow_null=True, allow_blank=True
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    is_active = serializers.BooleanField(read_only=True)
    is_email_verified = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "is_email_verified",
            "name",
            "email",
            "is_active",
            "last_login",
            "is_superuser",
            "is_staff",
        )

    def update(self, instance, validated_data):
        """
        # :param instance:
        # :param validated_data:
        # :return:
        #"""

        for key, value in validated_data.items():
            if key == "password":
                setattr(instance, key, make_password(value))
            else:
                setattr(instance, key, value)

        instance.save()
        return instance
