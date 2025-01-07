from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Post

admin.site.register(Post, TranslatableAdmin)
admin.site.register(Category, TranslatableAdmin)
