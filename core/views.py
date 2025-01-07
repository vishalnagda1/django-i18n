from django.contrib import messages
from django.shortcuts import render

from .models import Post


def index(request):
    if request.user.is_authenticated:
        messages.success(request, "Hi, welcome!", extra_tags="alert alert-success")
    else:
        messages.warning(
            request, "You are not authenticated!", extra_tags="alert alert-danger"
        )
    posts = Post.objects.all()

    context = {"posts": posts}
    return render(request, "index.html", context)
