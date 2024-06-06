from django.contrib import admin
from django.urls import path

from .views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
