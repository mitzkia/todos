from django.urls import path

from task import views as task_views


urlpatterns = [
    path('categories/', task_views.get_categories),
    path('categories/create/', task_views.create_category),
    path('categories/edit/<int:category_id>', task_views.edit_category),
    path('categories/delete/<int:category_id>', task_views.delete_category),
    path('category_tasks/<int:category_id>', task_views.get_category_tasks),
    path('tasks/', task_views.get_tasks),
    path('tasks/create/', task_views.create_task),
    path('tasks/edit/<int:task_id>', task_views.edit_task),
    path('tasks/delete/<int:task_id>', task_views.delete_task),
]
