from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from tinymce import models as tinymce_models


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='featured', blank=True)
    content = tinymce_models.HTMLField()
    published_date = models.DateTimeField(default=timezone.now(), editable=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-published_date',)

    @models.permalink
    def get_absolute_url(self):
        return ('post_url', (), {
            'post_id': self.id,
            })
