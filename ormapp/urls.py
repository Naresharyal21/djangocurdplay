from django.contrib import admin
from django.urls import path
 
from .import views

urlpatterns = [
    path("home/",views.homeview, name="home_url"),
    path("create/post/",views.create_Myblog,name="create_post_url"),
   path("blog/view/<id>/", views.blog_view, name="blog_view_url"),
   path("blog/delete/<int:id>/", views.delete_view, name="delete_blog_view_url"),
   
   path("blog/delete/conform/", views.delete_view_blog, name="conform_delete_blog_url"),

   path("blog/update/<int:id>/", views.update_view, name="update_blog_view_url"),

   path("update/blog/<id>/",views.update_Myblog,name="update_post_url"),
]