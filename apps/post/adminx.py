import xadmin

from post.models import Post, Tag, Category


class PostAdmin(object):
    list_display = ['title', 'pub_time', 'category', 'author']


class TagAdmin(object):
    list_display = ['name']


class CategoryAdmin(object):
    list_display = ['name', 'is_nav']


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
