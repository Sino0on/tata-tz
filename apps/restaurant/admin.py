from django.contrib import admin
from apps.restaurant.models import Restaurant, Review


admin.site.register(Restaurant)
admin.site.register(Review)
