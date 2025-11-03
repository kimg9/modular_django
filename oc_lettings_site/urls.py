from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
