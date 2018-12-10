from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task.models import Task, TaskCategory
from task.serializers import (
    TaskSerializer,
    CreateTaskSerializer,
    TaskCategorySerializer
)


@api_view(['GET'])
@never_cache
def get_categories(request):
    categories = TaskCategory.objects.all()
    serializer = TaskCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@never_cache
def get_tasks(request):
    tasks = Task.objects.all().select_related('category')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@never_cache
def get_category_tasks(request, category_id):
    category = get_object_or_404(
        TaskCategory,
        pk=category_id
    )
    serializer = TaskSerializer(
        category.tasks(manager='objects').all(),
        many=True
    )
    return Response(serializer.data)
    

@api_view(['POST'])
@never_cache
def create_category(request):
    serializer = TaskCategorySerializer(data=request.data)
    if serializer.is_valid():
        category = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@never_cache
def create_task(request):
    serializer = CreateTaskSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@never_cache
def edit_category(request, category_id):
    category = get_object_or_404(
        TaskCategory,
        pk=category_id
    )
    serializer = TaskCategorySerializer(category, data=request.data)
    if serializer.is_valid():
        category = serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@never_cache
def edit_task(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id
    )
    serializer = CreateTaskSerializer(task, data=request.data)
    if serializer.is_valid():
        task = serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@never_cache
def delete_category(request, category_id):
    category = get_object_or_404(
        TaskCategory,
        pk=category_id
    )
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@never_cache
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id
    )
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
