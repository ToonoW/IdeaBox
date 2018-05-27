from django.contrib import admin
from user_center import models


def register_model(model):
    """
    docstring here
    :param model: Model 类
    将传进来的模型的各个字段，及模型本身注册到后台管理界面
    """
    fields = list(model._meta.fields)
    fields.reverse()

    class ModelAdmin(admin.ModelAdmin):
        """
        Model管理模型
        """
        list_display = list(filter(lambda x: x != 'id', map(
            lambda x: x.name, fields)))

    admin.site.register(model, ModelAdmin)


# 取出所有需要注册的 Model, 将 Model 注册到后台管理上
NO_REGISTER_MODELS = ('auth_models',)
list(map(register_model, map(lambda classname: getattr(models, classname), filter(
    lambda x: '__' not in x and x != 'models' and x not in NO_REGISTER_MODELS, dir(models)))))
