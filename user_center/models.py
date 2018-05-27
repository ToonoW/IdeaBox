from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    
    avatar = models.ImageField('头像')
    wx_nickname = models.CharField('微信昵称', max_length=32, blank=True, null=True)
    nickname = models.CharField('昵称', max_length=32, blank=True, null=True) 

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
