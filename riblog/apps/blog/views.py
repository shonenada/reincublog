from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def index(request):
    query_set = Post.objects.all()
    p = Paginator(query_set, 10, orphans=3)
    page = request.GET.get('page')
    try:
        posts = p.page(page)
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(p.num_pages)
    return render_to_response('index.html', {'posts': posts}, context_instance=RequestContext(request))
