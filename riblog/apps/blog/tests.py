from django.test import TestCase

from .models import Post


class ViewTest(TestCase):
    fixtures = ['view_test.json']

    def test_single_post(self):
        # Bad url tests - all prepended with /post when called.
        for url in {
                '',
                'a/',
                '0/',
                '-1/',
                'post/1/',
                }:
            response = self.client.get('/post/'+url, follow=True)
            self.assertEqual(response.status_code, 404)

        # Find a first post and load it.
        test_post = Post.objects.all()[0]
        url = '/post/' + str(test_post.id)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
