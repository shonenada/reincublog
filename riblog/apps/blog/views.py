from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Post


def single(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse(post.title)
