from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib import admin
admin.autodiscover()

from apps.blog.models import Post


info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'published_date',
}


sitemaps = {
    'blog': GenericSitemap(info_dict, priority=1),
}


urlpatterns = patterns('',
    url(r'^$', 'riblog.apps.blog.views.index'),
    url(r'^post/', include('riblog.apps.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
