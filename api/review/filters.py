import django_filters
from apps.restaurant.models import Review


class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = ['rest']
