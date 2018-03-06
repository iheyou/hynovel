
from datetime import datetime

from django.db import models
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

# class RegisterForm(ModelForm):

#     class Meta():
#         model = User
#         fields = ['user_name', 'user_passwd']


# class Profile(models.Model):
#     user_image = models.ImageField(verbose_name='用户头像', null=True)
#     users = models.OneToOneField(User)


class NovelCategory(models.Model):
    category_name = models.CharField(max_length=20, null=False, verbose_name='分类名称')
    category_id = models.ImageField(max_length=50, default=0, verbose_name='分类id')

    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class Novel(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_identify = models.CharField(max_length=50, null=True)
    book_name = models.CharField(max_length=50, null=True, verbose_name='书名')
    book_image = models.CharField(max_length=200, verbose_name='封面', null=True)
    book_author = models.CharField(max_length=50, null=True, verbose_name='作者')
    book_category = models.CharField(
        max_length=50, null=True, verbose_name='分类')
    book_latest = models.CharField(
        max_length=50, null=True, verbose_name='更新时间')
    book_desc = models.CharField(max_length=1000, null=True, verbose_name='简介')

    book_click = models.IntegerField(default=0, verbose_name='点击数')
    book_clect = models.ImageField(default=0, verbose_name='收藏数')

    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '小说名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name


class Chapter(models.Model):
    chap_id = models.AutoField(primary_key=True)
    chap_identify = models.IntegerField()
    chap_title = models.CharField(max_length=100, null=True, verbose_name='章节')
    chap_contentUrl = models.CharField(
        max_length=100, null=True, verbose_name='内容链接')
    book_identify = models.CharField(max_length=50, null=False, default='')

    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.chap_title
