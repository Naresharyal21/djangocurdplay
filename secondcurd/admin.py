from django.contrib import admin

# Register your models here.
from .models import User , Mytask


admin.site.register(User)
admin.site.register(Mytask)