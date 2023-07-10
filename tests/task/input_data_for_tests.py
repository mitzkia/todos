CUSTOM_VALID_CATEGORY = {"id": 1, "name": "test-category"}
CUSTOM_VALID_CATEGORY2 = {"id": 1, "name": "new-test-category"}
CUSTOM_VALID_CATEGORY_WITH_HIGHER_ID = {"id": 100000, "name": "test-category"}
EMPTY_NAME_CATEGORY = {"id": 1, "name": ""}
CATEGORY_WITH_MISSING_ID_FIELD = {"name": "test-category"}
CATEGORY_WITH_MISSING_ID_FIELD2 = {"name": "test-category-2"}
CATEGORY_WITH_MISSING_NAME_FIELD = {"id": 1}
CATEGORY_WITH_LONG_NAME = {"id": 1, "name": "ABCDE" * 65563}
CATEGORY_WITH_UTF8_NAME = {"id": 1, "name": "ÁŐÚŰÖÜÓ"}
CATEGORY_WITH_INT_NAME = {"id": 1, "name": 65563}
CATEGORY_WITH_LIST_NAME = {
    "id": 1,
    "name": ["test-category", "test-category2", "test-category3"],
}

CUSTOM_VALID_TASK = {
    "title": "Task-title",
    "description": "Task-description",
    "category": 1,
    "deadline": "2023-01-01",
}

CUSTOM_VALID_TASK2 = {
    "title": "Task-title-2",
    "description": "Task-description-2",
    "category": 1,
    "deadline": "2023-01-02",
}

TASK_WITH_EMPTY_TITLE = {
    "title": "",
    "description": "Task-description",
    "category": 1,
    "deadline": "2023-01-01",
}

TASK_WITH_EMPTY_DESCRIPTION = {
    "title": "Task-title",
    "description": "",
    "category": 1,
    "deadline": "2023-01-01",
}

TASK_WITH_EMPTY_DATE = {
    "title": "Task-title",
    "description": "Task-description",
    "category": 1,
    "deadline": "",
}
