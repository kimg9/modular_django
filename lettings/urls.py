from django.urls import path

from . import views
from .apps import LettingsConfig


"""
This module defines the URL patterns for the `lettings` app.

@var app_name: The namespace for lettings URLs.
@var urlpatterns: List of URL patterns mapping URLs to view functions.
"""

app_name = LettingsConfig.name

urlpatterns = [
    path('lettings/', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
