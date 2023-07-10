from task.views import create_category
from task.views import create_task
from task.views import delete_category
from task.views import delete_task
from task.views import edit_category
from task.views import edit_task
from task.views import get_categories
from task.views import get_category_tasks
from task.views import get_tasks

SUCCESSFUL_STATUS_CODE_GROUP_PREFIX = "2"  # 2xx return codes
CLIENT_ERROR_STATUS_CODE_GROUP_PREFIX = "4"  # 4xx return codes


class TaskExecutor(object):
    def __init__(self, factory):
        self.factory = factory

    def get_categories(self):
        return get_categories(self.factory.get("/api/categories/"))

    def get_category_tasks(self, category_id):
        return get_category_tasks(
            self.factory.get(f"/api/category_tasks/{category_id}"), category_id
        )

    def get_tasks(self):
        return get_tasks(self.factory.get("/api/tasks/"))

    def create_category(self, input_category):
        return create_category(
            self.factory.post("/api/categories/create/", input_category)
        )

    def create_task(self, input_task):
        return create_task(self.factory.post("/api/tasks/create/", input_task))

    def edit_task(self, input_task, task_id):
        request = self.factory.put(
            f"/api/tasks/edit/{task_id}", input_task, content_type="application/json"
        )
        return edit_task(request, task_id)

    def edit_category(self, input_category, category_id):
        request = self.factory.put(
            f"/api/categories/edit/{category_id}",
            input_category,
            content_type="application/json",
        )
        return edit_category(request, category_id)

    def delete_category(self, category_id):
        return delete_category(
            self.factory.delete("/api/categories/delete/"), category_id
        )

    def delete_task(self, task_id):
        return delete_task(self.factory.delete("/api/tasks/delete/"), task_id)


class ResponseValidator(object):
    def __init__(self):
        pass

    def is_positive_response(self, response):
        return str(response.status_code)[0] == SUCCESSFUL_STATUS_CODE_GROUP_PREFIX

    def is_negative_response(self, response):
        return str(response.status_code)[0] == CLIENT_ERROR_STATUS_CODE_GROUP_PREFIX
