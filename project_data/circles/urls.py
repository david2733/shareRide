"""Circles URLs."""

# Django
from django.urls import path

# Views
from project_data.circles.views import create_circle, list_circles

urlpatterns = [
    path('circles/', list_circles),
    path('circles/create/', create_circle)
]
