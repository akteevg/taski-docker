"""Сериализаторы."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализаторв задач."""

    class Meta:
        """Класс мета."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
