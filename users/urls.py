from django.urls import path
from .views import get_profiles,create_profile

urlpatterns = [
    path('', get_profiles),
     path('create/', create_profile),
]