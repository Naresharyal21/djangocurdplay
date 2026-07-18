from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("curd/", include("curd.urls")),
    path("ormapp/",include("ormapp.urls")),
]