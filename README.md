uv venv --python 3.13
uv init .
uv add django
uv run django-admin startproject mysite .
uv run python manage.py migrate
uv run python manage.py runserver
uv run manage.py startapp core

- To make migrations for the app
uv run python manage.py makemigrations
- After creating the migration, we need to migrate the migration
uv run python manage.py migrate

- To create a superuser
uv run python manage.py createsuperuser