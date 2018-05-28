from django.shortcuts import render
from rest_framework import viewsets

from ideas import serializers, models


class IdeaViewset(viewsets.ModelViewSet):
    """想法"""
    serializer_class = serializers.IdeaSerializer
    queryset = models.Idea.objects.all()
