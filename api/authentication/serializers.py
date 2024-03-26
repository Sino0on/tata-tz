from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password1 = serializers.CharField()

    def validate_password1(self, password1):
        if not validate_password(password1):
            return password1

    def validate_username(self, username):
        if User.objects.filter(username=username, is_active=True).exists():
            raise serializers.ValidationError(
                _("Пользователь с таким логином уже зарегистрирован.")
            )
        return username

    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email', 'password1']


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email']
