# TODOs - A React exercise

## Introduction

The purpose of this exercise is to use the REST endpoints provided by this Django app, and implement a simple UI based on those using React.

The business logic of this app consists of two models: Task and TaskCategory. Each Task has a title, description, deadline and a reference to TaskCategory. Task categories have only names. We want to be able to list, create, edit and delete Tasks and TaskCategories. (See `task/urls.py`, `task/views.py` and `task/serializers.py` for implementation details.)

## Getting started

Clone this repository an cd into it.

Install Django and other dependencies. It is recommended to use the Python virtual environment to keep the requirements isolated.
Inside the project folder:

    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt

Migrate the database. We use sqlite3 here for simplicity

    python manage.py migrate

Create an initial superuser if you want to access the admin interface at /admin

    python manage.py createsuperuser

There is also a script for creating initial categories

    python manage.py init_categories

Install Yarn and then the dependencies in package.json

    yarn

Build the UI code. Webpack can also watch the files so that the code is re-built when files are changed.

    yarn run build (or) yarn run watch

Start the development server

    python manage.py runserver

The server should be now running on http://localhost:8000

## The Exercise

Start from `static/js/index.js`. Use the existing endpoints to list, create, edit and delete Tasks. You can use the initial categories generated by the script. Use also the endpoint for getting all the tasks in a specific category (/api/category_tasks/<int:category_id>).

The UI should look and feel nice and intuitive. Code quality also matters. Touching the backend code should not be necessary, but feel free to do so if needed.

Doing this exercise shouldn't take more than a day's work. You can submit it unfinished if you feel that too much time has been spent.

### Bonus 1

Implement a full CRUD for TaskCategories as well.

### Bonus 2

Write tests for the UI code.

### When you are done

Use git to commit your changes to their own branch and create a pull request.
