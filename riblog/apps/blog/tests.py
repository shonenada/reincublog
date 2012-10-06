from django.core.urlresolvers import reverse
from django.test import TestCase

from sorl.thumbnail import get_thumbnail

from .models import Post


class ViewTest(TestCase):
    fixtures = ['view_test.json']


    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Check first 10 posts are in home page.
        for test_post in Post.objects.all()[:10]:
            # Title of post should be in <h1> tags
            self.assertContains(response, '<h1>'+test_post.title+'</h1>')
            # Check that the post is linked to...
            url = '/post/' + str(test_post.id)
            self.assertContains(response, url)
        # Assume (naughty) that pagination works because of the lib.


    def test_single_post(self):
        # Bad url tests - all prepended with /post when called.
        for url in {
                '',
                'a/',
                '0/',
                '-1/',
                'post/1/',
                '1a/',
                }:
            response = self.client.get('/post/'+url, follow=True)
            self.assertEqual(response.status_code, 404)

        # Find a first post and load it.
        for test_post in Post.objects.all():
            url = '/post/' + str(test_post.id)
            response = self.client.get(url, follow=True)
            # Should be a valid page
            self.assertEqual(response.status_code, 200)
            # Title of post should be in <h1> tags
            self.assertContains(response, '<h1>'+test_post.title+'</h1>')
            # Post should contain the content
            self.assertContains(response, test_post.content)
            # Post should have a featured_image if there is one.
            if test_post.featured_image:
                thumb = get_thumbnail(test_post.featured_image, '400')
                self.assertContains(response, thumb.name)
            # There should be next and previous links if they exist.
            for direction in ('next', 'previous'):
                try:
                    next_prev = getattr(test_post, 'get_'+direction+'_by_published_date')()
                    self.assertContains(response, reverse('riblog.apps.blog.views.single', args=(next_prev.id,)))
                except Post.DoesNotExist:
                    pass
