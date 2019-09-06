from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    is_nav = models.BooleanField(verbose_name='是否是导航栏', default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=70)
    body = RichTextUploadingField(verbose_name='正文', config_name='post_config')
    pub_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category = models.ForeignKey(Category,verbose_name='分类', null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    views = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    author = models.ForeignKey(User, verbose_name='作者', null=True, blank=True, on_delete=models.SET_NULL)

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

