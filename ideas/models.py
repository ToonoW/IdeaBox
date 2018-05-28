from django.db import models

from user_center import models as user_models


class Idea(models.Model):

    title = models.CharField('标题', max_length=128)
    author = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, verbose_name='作者')
    content = models.TextField('内容')
    create_at = models.DateTimeField('创建于', auto_now_add=True)
    is_activate = models.BooleanField('激活状态', default=True)
    modify_at = models.DateTimeField('最后修改', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '想法'
        verbose_name_plural = '想法'
