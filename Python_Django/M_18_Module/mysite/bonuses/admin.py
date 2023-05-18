from django.contrib import admin
from .models import Promotion, Profile


@admin.register(Promotion)
class AdminPromotion(admin.ModelAdmin):
    list_display = "pk", "title", 
    list_display_links = ["pk", "title",]
    ordering = ["pk",]
    
    
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = "pk", "user",  
    list_display_links = ["pk", "user",]
    ordering = ["pk",]