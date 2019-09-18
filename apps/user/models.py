from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    mobile = models.CharField('手机号', max_length=15)
    nickname = models.CharField('昵称', max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
