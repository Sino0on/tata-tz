from api.restaurant.views import RestaurantModelViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', RestaurantModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]

