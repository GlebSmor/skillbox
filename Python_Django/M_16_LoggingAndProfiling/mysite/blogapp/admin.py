from django.contrib import admin

from .models import *


@admin.register(Article)
class  ArticleAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "category_verbose", "author_verbose", "pub_date"
    list_display_links = "pk", "title"
    ordering = "pk",
    
    def author_verbose(self, obj: Article):
        return obj.author.name
    
    def category_verbose(self, obj: Article):
        return obj.category.name
        
    
    
@admin.register(Author)
class  ArticleAuthor(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
    ordering = "pk",


@admin.register(Category)
class  ArticleCategory(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
    ordering = "pk",


@admin.register(Tag)
class  ArticleTag(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
    ordering = "pk",


