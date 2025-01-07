from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Post


# Modify admin panel using TranslatableAdmin
class MyAdminPanel(TranslatableAdmin):
    # Extend admin with search field.
    search_fields = [
        "category__translations__name__icontains",  # using category prefix because this is our foreign key
        "translations__title__icontains",
        "translations__content__icontains",
    ]


admin.site.register(Post, MyAdminPanel)
admin.site.register(Category, TranslatableAdmin)
