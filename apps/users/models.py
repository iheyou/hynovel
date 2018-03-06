from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    user_name = models.CharField(max_length=18, verbose_name='用户名')
    user_passwd = models.CharField(max_length=18, verbose_name='密码')
    user_nickname = models.CharField(
        max_length=20, verbose_name='昵称', default=user_name)
    user_email = models.CharField(max_length=18, verbose_name='邮箱', null=True)
    user_image = models.ImageField(verbose_name='用户头像', null=True)

    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name


class UserCollectNovels(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    novel_identify = models.CharField(max_length=50, null=False, verbose_name='小说标识')
    novel_name = models.CharField(max_length=50, default=None, verbose_name='书名')
    novel_image = models.ImageField(verbose_name='小说封面', null=True)
    novel_author = models.CharField(max_length=50, null=True, verbose_name='作者')
    novel_latest = models.CharField(max_length=50, null=True, verbose_name='最后更新')
    add_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '书架'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.novel_name
