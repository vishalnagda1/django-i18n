from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Post


def index(request):
    if request.user.is_authenticated:
        messages.success(request, _("login-auth-message {}").format(request.user.first_name), extra_tags="alert alert-success")
    else:
        messages.warning(
            request, _("logout-auth-message"), extra_tags="alert alert-danger"
        )
    posts = Post.objects.all()

    context = {"posts": posts}
    return render(request, "index.html", context)
