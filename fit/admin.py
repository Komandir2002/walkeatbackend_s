from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Menu, Category, Tag

# Register your models here.
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Tag)