from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<post_id>\d+)/$', 'riblog.apps.blog.views.single'),
)
