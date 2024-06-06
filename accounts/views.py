from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout

from .models import User
from .serializers import RegistrationSerializer


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key

            data = {'email': user.email, 'token': token}
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user and user.is_active:
            if not check_password(password, user.password):
                data = {'message': 'Incorrect password'}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = {}
            token = Token.objects.get_or_create(user=user)[0].key
            data['token'] = token
            data['email'] = email
            login(request, user)
            return Response(data, status=status.HTTP_200_OK)

        else:
            data = {'message': 'User with this email not exist'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        logout(request)
        data = {"message": "Logout successful"}
        return Response(data, status=status.HTTP_200_OK)
