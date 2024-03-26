from api.review.views import ReviewModelViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', ReviewModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]

