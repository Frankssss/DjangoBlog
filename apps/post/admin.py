__author__ = "Frank Shen"

from django.contrib import admin

from post.models import Post, Tag, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_time', 'category', 'author']
    fields = (('title','author'), 'body', ('category', 'tags'))
    actions_on_bottom = False
    actions_selection_counter = False
    date_hierarchy = 'pub_time'
    list_filter = ('tags', 'category')
    list_per_page = 10
    # radio_fields = {"author": admin.HORIZONTAL}
    raw_id_fields = ("tags", )
    search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
    actions_on_bottom = False
    actions_selection_counter = False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_nav']
    list_per_page = 10
    search_fields = ['name']
    list_filter = ('is_nav', )
    actions_on_bottom = False
    actions_selection_counter = False