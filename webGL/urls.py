from django.contrib import admin
from django.urls import path, include
# from . import UnityDemo
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome_page'),
    path('unity/', views.unit, name='sim_page'),
]