from django.contrib import admin
from django.urls import path
 
from .import views

urlpatterns = [
    path("home/",views.homeview, name="home_url"),
    path("create/post/",views.create_Myblog,name="create_post_url"),
   
]