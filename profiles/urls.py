from django.urls import path

from . import views
from .apps import ProfilesConfig


"""
This module defines the URL patterns for the `profiles` app.

@var app_name: The namespace for profiles URLs.
@var urlpatterns: List of URL patterns mapping URLs to view functions.
"""

app_name = ProfilesConfig.name
urlpatterns = [
    path('profiles/', views.index, name='index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
