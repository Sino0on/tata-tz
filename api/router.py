from django.urls import path, include


urlpatterns = [
    path("restaurant/", include("api.restaurant.urls")),
    path("review/", include("api.review.urls")),
    path("auth/", include("api.authentication.urls")),
    path("docs/", include("api.openapi.urls")),
]
