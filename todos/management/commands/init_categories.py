from django.core.management.base import BaseCommand

from task.models import TaskCategory


class Command(BaseCommand):

    help = 'Create test categories'

    def handle(self, *args, **options):
        print("Creating test categories...")
        category_names = ['School', 'Work', 'Other', 'Christmas']
        for name in category_names:
            task, created = TaskCategory.objects.get_or_create(name=name)
        print("Created.")
