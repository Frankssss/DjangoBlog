from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from post.models import Post


class Comment(MPTTModel):

    content = models.TextField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )
    reply_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replyers'
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name
