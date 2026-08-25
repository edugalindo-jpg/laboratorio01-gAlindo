from django.urls import path

from . import views

app_name = "session1"

urlpatterns = [
    path("bienvenido/", views.bienvenido, name="bienvenido"),
]
