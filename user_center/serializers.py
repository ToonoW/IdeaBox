from rest_framework import serializers

from user_center import models


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'nickname', 'wx_nickname', 'username', 'email',)
