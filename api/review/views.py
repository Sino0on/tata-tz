from rest_framework.response import Response

from apps.restaurant.models import Restaurant, Review
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from api.restaurant.pagination import MyLimitPagination
from api.restaurant.permissions import CanChangeRestaraunt
from api.review.filters import ReviewFilter
from api.review.serializers import ReviewSerializer


class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = MyLimitPagination
    permission_classes = (CanChangeRestaraunt,)
    filterset_class = ReviewFilter
    ordering_fields = ['title', 'created_at']

