from django.shortcuts import get_object_or_404, render_to_response

from .models import Post


def single(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('single_post.html', {'post': post})
