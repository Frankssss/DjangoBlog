from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    confirmed = models.BooleanField(default=False)
    nickname = models.CharField('昵称', max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('MyUser', on_delete=models.CASCADE, )
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"