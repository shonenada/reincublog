from django.shortcuts import get_object_or_404, render_to_response

from .models import Post


def single(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    data = {'post': post}
    for direction in ('next', 'previous'):
        try:
            data[direction] = getattr(post, 'get_'+direction+'_by_published_date')()
        except Post.DoesNotExist:
            pass
    return render_to_response('single_post.html', data)
