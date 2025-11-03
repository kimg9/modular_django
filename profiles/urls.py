from django.urls import path

from . import views
from .apps import ProfilesConfig

app_name = ProfilesConfig.name
urlpatterns = [
    path('profiles/', views.index, name='index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
