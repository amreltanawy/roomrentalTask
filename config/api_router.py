from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from hotel_room_reservation.reservations.views import ReservationViewSet
from hotel_room_reservation.users.api.views import UserViewSet

if settings.DEBUG:
    Router = DefaultRouter
else:
    Router = SimpleRouter

user_router = Router()
user_router.register("users", UserViewSet)

reservations_router = Router()
reservations_router.register("reservations", ReservationViewSet, basename='reservations')


urlpatterns = user_router.urls
urlpatterns += reservations_router.urls
