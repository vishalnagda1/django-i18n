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

- To translating our model we use library called django-parler
uv add django-parler

- add django-parler to project settings in installed apps

Note: Once you update your app models to make them translatable using django-parler. Then you have to create a migration. If you try to migrate with that migration then you will get an error in the console - `raise TypeError(
        f"Translatable model {shared_model} does not appear to inherit from TranslatableModel"
    )`. To fix it you need to select your migration file and update the bases. You need to change from `bases=(parler.models.TranslatedFieldsModelMixin, models.Model)` to `bases=(parler.models.TranslatableModel, models.Model)`. Now try to migrate again.
