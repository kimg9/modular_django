from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views


"""
This module defines the URL patterns for the main OC Lettings Site project.

@var urlpatterns: List of URL patterns mapping URLs to project-level views and included app URLs.
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
