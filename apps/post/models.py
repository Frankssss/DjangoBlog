from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

import markdown


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_nav = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    mod_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'posts'
        ordering = ["-pub_time"]
        verbose_name = '文章'
        verbose_name_plural = verbose_name

