from django.urls import path

from . import views
from .apps import LettingsConfig


app_name = LettingsConfig.name

urlpatterns = [
    path('lettings/', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
