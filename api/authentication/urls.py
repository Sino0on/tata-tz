from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from api.authentication.views import UserRegisterView, CustomTokenObtainView, GetMeApiView


urlpatterns = [
    path("token/", CustomTokenObtainView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    path("users/me/", GetMeApiView.as_view()),
    path('users/register/', UserRegisterView.as_view())
]
