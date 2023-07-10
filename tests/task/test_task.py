from collections import OrderedDict

from django.test import TestCase
from django.test.client import RequestFactory

from tests.task.common import ResponseValidator
from tests.task.common import TaskExecutor
from tests.task.input_data_for_tests import CUSTOM_VALID_CATEGORY
from tests.task.input_data_for_tests import CUSTOM_VALID_TASK
from tests.task.input_data_for_tests import CUSTOM_VALID_TASK2
from tests.task.input_data_for_tests import TASK_WITH_EMPTY_DATE
from tests.task.input_data_for_tests import TASK_WITH_EMPTY_DESCRIPTION
from tests.task.input_data_for_tests import TASK_WITH_EMPTY_TITLE


class TaskTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.task_executor = TaskExecutor(self.factory)
        self.response_validator = ResponseValidator()

    def order_fields_in_tasks_data(self, task_data):
        return [OrderedDict(sorted(dict(task_data[0]).items()))]

    def test_get_from_empty_task(self):
        # check if getting tasks list works without creating any new tasks
        self.assertEqual(self.task_executor.get_tasks().data, [])

    def test_create_new_task(self):
        # check if creating new custom task works, and also check if it is listable
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        CUSTOM_VALID_TASK.update({"category": CUSTOM_VALID_CATEGORY["id"], "id": 1})
        response = self.task_executor.create_task(CUSTOM_VALID_TASK)
        self.assertTrue(self.response_validator.is_positive_response(response))

        CUSTOM_VALID_TASK.update({"category": OrderedDict(CUSTOM_VALID_CATEGORY)})
        self.assertEqual(
            self.order_fields_in_tasks_data(self.task_executor.get_tasks().data),
            [OrderedDict(sorted(CUSTOM_VALID_TASK.items()))],
        )

    def test_create_task_without_category(self):
        # check if creating new task without category does not work
        CUSTOM_VALID_TASK.update({"category": 1, "id": 1})
        response = self.task_executor.create_task(CUSTOM_VALID_TASK)
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_tasks().data, [])

    def test_create_task_with_empty_title(self):
        # check if creating new task with empty title works (let assume this is the expected behaviour)
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        TASK_WITH_EMPTY_TITLE.update({"category": CUSTOM_VALID_CATEGORY["id"], "id": 1})
        response = self.task_executor.create_task(TASK_WITH_EMPTY_TITLE)
        self.assertTrue(self.response_validator.is_positive_response(response))

        TASK_WITH_EMPTY_TITLE.update({"category": OrderedDict(CUSTOM_VALID_CATEGORY)})
        self.assertEqual(
            self.order_fields_in_tasks_data(self.task_executor.get_tasks().data),
            [OrderedDict(sorted(TASK_WITH_EMPTY_TITLE.items()))],
        )

    def test_create_task_with_empty_description(self):
        # check if creating new task with empty description does not work (let assume this is the expected behaviour)
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        TASK_WITH_EMPTY_DESCRIPTION.update(
            {"category": CUSTOM_VALID_CATEGORY["id"], "id": 1}
        )
        response = self.task_executor.create_task(TASK_WITH_EMPTY_DESCRIPTION)
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_tasks().data, [])

    def test_create_task_with_empty_date(self):
        # check if creating new task with empty date does not work (let assume this is the expected behaviour)
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        TASK_WITH_EMPTY_DATE.update({"category": CUSTOM_VALID_CATEGORY["id"], "id": 1})
        response = self.task_executor.create_task(TASK_WITH_EMPTY_DATE)
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_tasks().data, [])

    def test_create_multiple_different_tasks(self):
        # check if creating multiple tasks works, and they are listable (also individually)
        expected_counter = 2
        for counter in range(1, expected_counter + 1):
            new_category = {"id": counter, "name": f"test-category-{counter}"}
            self.task_executor.create_category(new_category)

            new_task = {
                "title": f"Task-title-{counter}",
                "description": f"Task-description-{counter}",
                "category": counter,
                "deadline": "2023-01-01",
                "id": counter,
            }
            self.task_executor.create_task(new_task)

            new_task.update({"category": OrderedDict(new_category)})
            self.assertEqual(
                self.order_fields_in_tasks_data(
                    self.task_executor.get_category_tasks(new_category["id"]).data
                ),
                [OrderedDict(sorted(new_task.items()))],
            )

        self.assertEqual(len(self.task_executor.get_tasks().data), expected_counter)

    def test_edit_task(self):
        # check if editing task works, and changes are saved
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        CUSTOM_VALID_TASK.update({"category": CUSTOM_VALID_CATEGORY["id"], "id": 1})
        self.task_executor.create_task(CUSTOM_VALID_TASK)

        response = self.task_executor.edit_task(
            CUSTOM_VALID_TASK2, CUSTOM_VALID_TASK["id"]
        )
        self.assertTrue(self.response_validator.is_positive_response(response))
        CUSTOM_VALID_TASK2.update(
            {"category": OrderedDict(CUSTOM_VALID_CATEGORY), "id": 1}
        )

        self.assertEqual(
            self.order_fields_in_tasks_data(self.task_executor.get_tasks().data),
            [OrderedDict(sorted(CUSTOM_VALID_TASK2.items()))],
        )

    def test_edit_non_existing_task(self):
        # check if editing non existing task does not work
        response = self.task_executor.edit_task(CUSTOM_VALID_TASK2, 1)
        self.assertTrue(self.response_validator.is_negative_response(response))

    def test_delete_task(self):
        # check if deleting task works, and changes are saved
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        CUSTOM_VALID_TASK.update({"category": CUSTOM_VALID_CATEGORY["id"], "id": 1})
        self.task_executor.create_task(CUSTOM_VALID_TASK)
        self.assertEqual(len(self.task_executor.get_tasks().data), 1)

        response = self.task_executor.delete_task(CUSTOM_VALID_TASK["id"])
        self.assertTrue(self.response_validator.is_positive_response(response))
        self.assertEqual(len(self.task_executor.get_tasks().data), 0)

    def test_delete_non_existing_task(self):
        # check if deleting non existing task does not work
        response = self.task_executor.delete_task(1)
        self.assertTrue(self.response_validator.is_negative_response(response))
