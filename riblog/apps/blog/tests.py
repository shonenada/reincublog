from django.test import TestCase


class ViewTest(TestCase):
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
