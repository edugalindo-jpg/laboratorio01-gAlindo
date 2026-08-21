from django.urls import path
from . import views

urlpatterns = [
    path('bienvenido/', views.bienvenido, name='bienvenido'),
]