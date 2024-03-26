from apps.restaurant.models import Restaurant, Review
from rest_framework import viewsets
from django_filters import rest_framework as filters
from api.restaurant.pagination import MyLimitPagination
from api.restaurant.permissions import CanChangeRestaraunt
from api.restaurant.filters import RestaurantFilter
from api.restaurant.serializers import RestaurantSerializer


class RestaurantModelViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = MyLimitPagination
    permission_classes = (CanChangeRestaraunt,)
    filterset_class = RestaurantFilter
    ordering_fields = ['title', 'created_at']


