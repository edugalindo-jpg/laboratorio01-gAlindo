"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""

from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path(
        "",
        RedirectView.as_view(pattern_name="session1:bienvenido", permanent=False),
        name="home",
    ),
    path("session1/", include("session1.urls")),
]
