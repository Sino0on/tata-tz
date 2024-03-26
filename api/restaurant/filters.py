import django_filters
from apps.restaurant.models import Restaurant
from django.db.models import Q


class RestaurantFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', method='filter_title')
    category = django_filters.Filter(field_name='category')

    def filter_title(self, queryset, name, value):
        search_term = value
        queryset = queryset.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
        return queryset

    class Meta:
        model = Restaurant
        fields = ['title']
