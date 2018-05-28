from rest_framework import serializers

from ideas import models


class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Idea
        fields = (
            'title', 'author', 'content', 'create_at', 'is_activate', 'modify_at',)
        read_only_fields = ('create_at', 'modify_at', 'author',)
