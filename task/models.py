from django.db import models


class TaskCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Task Category'
        verbose_name_plural = 'Task Categories'

    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey(
        TaskCategory,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    deadline = models.DateField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
