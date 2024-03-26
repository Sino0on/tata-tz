from apps.restaurant.models import Restaurant, Review
from rest_framework import serializers
from django.db.models import Avg


class RestaurantSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)

    def get_rating(self, obj):
        average_rating = obj.reviews.all().aggregate(average_rating=Avg('rating'))
        return average_rating['average_rating']

    class Meta:
        model = Restaurant
        fields = ['id', 'title', 'description', 'image', 'address', 'rating']


class ReviewSerializer(serializers.ModelSerializer):
    rest = RestaurantSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
