from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from .views import *

urlpatterns = [
    path('generate_agora_token/', generate_agora_token, name='generate_agora_token'),
    path('', index, name='index'),
    path('home', home, name='home')
    ]