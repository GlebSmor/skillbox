from django.contrib import admin
from .models import *


@admin.register(HouseType)
class HouseAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = ["pk", "name"]
    ordering = ["pk",]
    
    
@admin.register(RoomsCount)
class HouseAdmin(admin.ModelAdmin):
    list_display = 'pk', 'count'
    list_display_links = ["pk",]
    ordering = ["pk",]


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'address', 'price'
    list_display_links = ["pk", "name"]
    ordering = ["pk",]
    
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title'
    list_display_links = ["pk", "title"]
    ordering = ["pk",]