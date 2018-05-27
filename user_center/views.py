from django.shortcuts import render
from rest_framework import viewsets

from user_center import serializers, models


class UserViewset(viewsets.ModelViewSet):
    """用户"""
    serializer_class = serializers.UserSerializers
    queryset = models.User.objects.all()
    