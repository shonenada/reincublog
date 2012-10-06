from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='featured', blank=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
