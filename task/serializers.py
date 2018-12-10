from rest_framework import serializers

from task.models import Task, TaskCategory


class TaskCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskCategory
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    category = TaskCategorySerializer()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'category',
            'deadline',
        )


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'category',
            'deadline',
        )
