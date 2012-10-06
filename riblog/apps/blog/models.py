from django.contrib.auth.models import User
from django.db import models

from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='featured', blank=True)
    content = tinymce_models.HTMLField()
    published_date = models.DateTimeField(auto_now_add=True, editable=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-published_date',)
