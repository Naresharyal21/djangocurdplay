from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test_api),
    path("home/", views.home_api),
]