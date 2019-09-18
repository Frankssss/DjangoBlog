from django.db import models
from django.contrib.auth.models import User
from user.models import MyUser

from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )
    root = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='root_comment'
    )
    reply_to = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='repliers'
    )
    post = models.ForeignKey(
        Post,
        related_name='post_comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        MyUser,
        related_name='user_comments',
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comments'
        ordering = ['created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name
