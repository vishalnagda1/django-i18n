from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("title"), max_length=200)
    content = models.TextField(_("content"))

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title
