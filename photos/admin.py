from django.contrib import admin
from .models import Name,Image,tags

# class Picture(admin.)

# Register your models here.
admin.site.register(Image)
admin.site.register(Name)
admin.site.register(tags)
