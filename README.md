# Django 118n

The project is created to take idea how internationalization works in the django framework.

### Project Setup
- I prefer to use [uv](https://docs.astral.sh/uv/) package manager. It's similar to [poetry](https://python-poetry.org/).
    
    - Create a virtual env with the python version of your choice (It will install the python automatically for your project)
        ```shell
        uv venv --python 3.13
        ```
    
    - Initialize the uv environment
        ```shell
        uv init .
        ```
    
    - To install existing packages
        ```shell
        uv sync
        ```
    
    - To install a new package
        ```shell
        uv add django
        ```

- To start a new django project
    ```shell
    uv run django-admin startproject mysite .
    ```

    - Run the migration
        ```shell
        uv run python manage.py migrate
        ```

- To run the project server
    ```shell
    uv run python manage.py runserver
    ```

- To create a new app in the django project
    ```shell
    uv run manage.py startapp core
    ```

    - To make migrations for the app
        ```shell
        uv run python manage.py makemigrations
        ```

    - After creating the migration, we need to migrate the migration
        ```shell
        uv run python manage.py migrate
        ```

- To create a django admin superuser
    ```shell
    uv run python manage.py createsuperuser
    ```

- For Internationalization support, we need to install `gettext` as system package. (I use ubuntu, you can install it as per your Operating System)
    ```shell
    sudo apt-get install gettext
    ```

- Create po file for translation
    ```shell
    uv run django-admin makemessages --all
    ```

- To compile po files to make mo files
    ```shell
    uv run django-admin compilemessages
    ```

- To edit the po file we need `django-rosetta` library
    ```shell
    uv add django-rosetta
    ```

- add `django-rosetta` to project [settings](mysite/settings.py) in installed apps.

- To translating our model we use library called `django-parler`.
    ```shell
    uv add django-parler
    ```

- add `django-parler` to project [settings](mysite/settings.py) in installed apps.
    
    - **Note:** *Once you update your app models to make them translatable using django-parler. Then you have to create a migration. If you try to migrate with that migration then you will get an error in the console - `raise TypeError(f"Translatable model {shared_model} does not appear to inherit from TranslatableModel")`. To fix it, you need to select your migration file and update the `bases` variable. You need to update from `bases=(parler.models.TranslatedFieldsModelMixin, models.Model)` to `bases=(parler.models.TranslatableModel, models.Model)`. Now try to migrate again.*

### Running the project:
- To install project dependencies
    ```shell
    uv sync
    ```

- To run the project server
    ```shell
    uv run python manage.py runserver
    ```


### Troubleshoot:
- If your project changes are not reflecting after making changes.
    ```shell
    find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
    ```
