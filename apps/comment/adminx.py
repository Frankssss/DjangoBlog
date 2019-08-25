__author__ = "Frank Shen"

import xadmin

from .models import Comment


class CommentAdmin(object):
    list_display = ['post', 'parent', ]


xadmin.site.register(Comment, CommentAdmin)