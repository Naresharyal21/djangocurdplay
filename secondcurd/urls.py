from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 path("signup/",views.signup, name="signup_view_url"),
 
 path("sigin/",views.signin, name="signin_view_url"),
 path("home/",views.home, name="home_url"),

 path("delete/",views.delete_user,name="delete_user_url"),
 path("update/",views.update_user,name="update_url"),

]