from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from .models import Post


def single(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    data = {'post': post}
    for direction in ('next', 'previous'):
        try:
            data[direction] = getattr(post, 'get_'+direction+'_by_published_date')()
        except Post.DoesNotExist:
            pass
    return render_to_response('single_post.html', data, context_instance=RequestContext(request))


def index(request, page_num):
    if page_num == '0':
        # Page zero is 404
        raise Http404
    elif page_num == '1':
        # Page one should always be the root of the blog.
        return redirect('/')
    elif page_num is None:
        # This is the root of the blog, page_num is 1.
        page_num = 1
    else:
        # else page number was 2 or more, so is fine. Just make it int.
        page_num = int(page_num)

    query_set = Post.objects.all()
    p = Paginator(query_set, 10, orphans=3)

    try:
        posts = p.page(page_num)
    except EmptyPage:
        # There is no content here - return a 404.
        raise Http404
    return render_to_response('index.html', {'posts': posts}, context_instance=RequestContext(request))
