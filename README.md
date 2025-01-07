uv venv --python 3.13
uv init .
uv add django
uv run django-admin startproject mysite .
uv run python manage.py migrate
uv run python manage.py runserver
uv run manage.py startapp core
