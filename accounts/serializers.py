from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')
        extra_kwargs = {
            "password": {"write_only": True},
            "confirm_password": {"write_only": True}
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm password did not match")

        data['password'] = make_password(password)
        return super().validate(data)
