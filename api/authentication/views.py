from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.translation import gettext_lazy as _
from api.authentication.serializers import UserRegisterSerializer, UserGetSerializer
from rest_framework.throttling import ScopedRateThrottle


User = get_user_model()


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": _("Неправильный логин или пароль")
    }


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        refresh = super().get_token(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return data


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    throttle_classes = [ScopedRateThrottle]
    permission_classes = (AllowAny,)
    throttle_scope = 'auth'

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User(
            first_name=serializer.validated_data.get("first_name"),
            last_name=serializer.validated_data.get("last_name"),
            email=serializer.validated_data.get("email"),
            username=serializer.validated_data.get('username')
        )

        user.set_password(serializer.validated_data.get('password'))
        user.save()
        das = MyTokenObtainPairSerializer()
        tokens = das.get_token(user=user)
        data = {
            'user': UserGetSerializer(user).data,
            "tokens": tokens
        }
        return Response(data, status=status.HTTP_200_OK)


class GetMeApiView(APIView):
    """Позволяет пользователю получить информацию о себе"""
    serializer_class = UserGetSerializer

    def get(self, request):
        user = self.request.user

        return Response(
            {
                "user": UserGetSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )