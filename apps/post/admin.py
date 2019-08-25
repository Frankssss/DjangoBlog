__author__ = "Frank Shen"

from django.contrib import admin

from post.models import Post, Tag, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_time', 'category', 'author']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_nav']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)