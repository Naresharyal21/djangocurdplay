from django.contrib import admin
from .models import Post, Profile ,Like ,User,Myblog
# Register your models here.
admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#   list_display=(
#     "username",
#     "created_at",
#     "updated_at",
#   )
  





admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Myblog)


