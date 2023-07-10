from collections import OrderedDict

from django.test import TestCase
from django.test.client import RequestFactory

from tests.task.common import ResponseValidator
from tests.task.common import TaskExecutor
from tests.task.input_data_for_tests import CATEGORY_WITH_INT_NAME
from tests.task.input_data_for_tests import CATEGORY_WITH_LONG_NAME
from tests.task.input_data_for_tests import CATEGORY_WITH_MISSING_ID_FIELD
from tests.task.input_data_for_tests import CATEGORY_WITH_MISSING_ID_FIELD2
from tests.task.input_data_for_tests import CATEGORY_WITH_MISSING_NAME_FIELD
from tests.task.input_data_for_tests import CATEGORY_WITH_UTF8_NAME
from tests.task.input_data_for_tests import CUSTOM_VALID_CATEGORY
from tests.task.input_data_for_tests import CUSTOM_VALID_CATEGORY2
from tests.task.input_data_for_tests import CUSTOM_VALID_CATEGORY_WITH_HIGHER_ID
from tests.task.input_data_for_tests import EMPTY_NAME_CATEGORY


class CategoryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.task_executor = TaskExecutor(self.factory)
        self.response_validator = ResponseValidator()

    def test_get_from_empty_category(self):
        # check if getting categories list works without creating any new categories
        self.assertEqual(self.task_executor.get_categories().data, [])

    def test_create_new_category(self):
        # check if creating new custom category works, and also check if it is listable
        response = self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        self.assertTrue(self.response_validator.is_positive_response(response))
        self.assertEqual(
            self.task_executor.get_categories().data,
            [OrderedDict(CUSTOM_VALID_CATEGORY)],
        )

    def test_create_category_with_higher_id_value(self):
        # check if creating new custom category with higher id number, creates category with default lower id
        response = self.task_executor.create_category(
            CUSTOM_VALID_CATEGORY_WITH_HIGHER_ID
        )
        self.assertTrue(self.response_validator.is_positive_response(response))

        CUSTOM_VALID_CATEGORY_WITH_HIGHER_ID.update({"id": 1})
        self.assertEqual(
            self.task_executor.get_categories().data,
            [OrderedDict(CUSTOM_VALID_CATEGORY_WITH_HIGHER_ID)],
        )

    def test_create_category_with_empty_name(self):
        # check if creating new custom category with empty name property results with an error message, and category not created
        response = self.task_executor.create_category(EMPTY_NAME_CATEGORY)
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_categories().data, [])

    def test_create_category_with_missing_name(self):
        # check if creating new custom category without name property results with an error message, and category not created
        response = self.task_executor.create_category(CATEGORY_WITH_MISSING_NAME_FIELD)
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_categories().data, [])

    def test_create_category_with_long_name(self):
        # check if creating new custom category with longer name property results with an error message, and category not created
        response = self.task_executor.create_category(CATEGORY_WITH_LONG_NAME)
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_categories().data, [])

    def test_create_category_with_utf8_name(self):
        # check if creating new custom category with UTF8 name property works, and category created
        response = self.task_executor.create_category(CATEGORY_WITH_UTF8_NAME)
        self.assertTrue(self.response_validator.is_positive_response(response))
        self.assertEqual(
            self.task_executor.get_categories().data,
            [OrderedDict(CATEGORY_WITH_UTF8_NAME)],
        )

    def test_create_category_with_int_type_name(self):
        # check if creating new custom category with int type name property works, and category created with casted name
        response = self.task_executor.create_category(CATEGORY_WITH_INT_NAME)
        self.assertTrue(self.response_validator.is_positive_response(response))
        CATEGORY_WITH_INT_NAME.update({"name": str(CATEGORY_WITH_INT_NAME["name"])})
        self.assertEqual(
            self.task_executor.get_categories().data,
            [OrderedDict(CATEGORY_WITH_INT_NAME)],
        )

    def test_create_categories_without_id(self):
        # check if creating new custom categories without id field works, and categories are created with sequential ids
        response = self.task_executor.create_category(CATEGORY_WITH_MISSING_ID_FIELD)
        self.assertTrue(self.response_validator.is_positive_response(response))
        response = self.task_executor.create_category(CATEGORY_WITH_MISSING_ID_FIELD2)
        self.assertTrue(self.response_validator.is_positive_response(response))

        CATEGORY_WITH_MISSING_ID_FIELD.update({"id": 1})
        CATEGORY_WITH_MISSING_ID_FIELD2.update({"id": 2})
        self.assertEqual(
            self.task_executor.get_categories().data,
            [
                OrderedDict(sorted(CATEGORY_WITH_MISSING_ID_FIELD.items())),
                OrderedDict(sorted(CATEGORY_WITH_MISSING_ID_FIELD2.items())),
            ],
        )

    def test_create_multiple_categories(self):
        # check if creating multiple new categories works, and categories are created with sequential ids
        expected_counter = 2
        for counter in range(1, expected_counter + 1):
            self.task_executor.create_category(
                {"id": counter, "name": f"test-category-{counter}"}
            )

        self.assertEqual(
            len(self.task_executor.get_categories().data), expected_counter
        )

    def test_edit_category(self):
        # check if editing category works, and changes are saved
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        response = self.task_executor.edit_category(
            CUSTOM_VALID_CATEGORY2, CUSTOM_VALID_CATEGORY["id"]
        )
        self.assertTrue(self.response_validator.is_positive_response(response))
        self.assertEqual(
            self.task_executor.get_categories().data,
            [OrderedDict(CUSTOM_VALID_CATEGORY2)],
        )

    def test_edit_non_existing_category(self):
        # check if editing non existing category does not work
        response = self.task_executor.edit_category(
            CUSTOM_VALID_CATEGORY2, CUSTOM_VALID_CATEGORY["id"]
        )
        self.assertTrue(self.response_validator.is_negative_response(response))

    def test_delete_category(self):
        # check if deleting category works, and changes are saved
        self.task_executor.create_category(CUSTOM_VALID_CATEGORY)
        self.assertEqual(
            self.task_executor.get_categories().data,
            [OrderedDict(CUSTOM_VALID_CATEGORY)],
        )

        response = self.task_executor.delete_category(CUSTOM_VALID_CATEGORY["id"])
        self.assertTrue(self.response_validator.is_positive_response(response))
        self.assertEqual(self.task_executor.get_categories().data, [])

    def test_delete_non_existing_category(self):
        # check if deleting non existing category does not work
        response = self.task_executor.delete_category(CUSTOM_VALID_CATEGORY["id"])
        self.assertTrue(self.response_validator.is_negative_response(response))
        self.assertEqual(self.task_executor.get_categories().data, [])
