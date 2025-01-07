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

- For Internationalization support, we need to install gettext.
sudo apt-get install gettext

- Create po file for translation
uv run django-admin makemessages --all
or
uv run python manage.py makemessages --all

- To compile po files to make mo files
uv run python manage.py compilemessages

- To edit the po file we need django-rosetta library
uv add django-rosetta

- add django-rosetta to project settings in installed apps
