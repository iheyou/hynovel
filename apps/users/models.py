from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    user_nickname = models.CharField(max_length=50, verbose_name='昵称', default='用户')
    user_mobile_phone = models.ImageField(max_length=15, null=True, blank=True, verbose_name='手机号码')
    user_image = models.ImageField(upload_to='user', verbose_name='用户头像', null=True, blank=True)

    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
