from django.db import models
from ProbitHome import settings
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from markdownx.models import MarkdownxField

# https://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
# https://stackoverflow.com/questions/25767787/django-cannot-create-migrations-for-imagefield-with-dynamic-upload-to-value/25768034
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}{}.{}'.format(Post.title,"_header", ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("images")


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# eventually implement the unsplash api to let user choose pertinent header images at # HERE
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = MarkdownxField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    Header = models.ImageField(upload_to=path_and_rename, default='https://source.unsplash.com/random/1920x1080')  # HERE

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author + " - " + self.body[0:25]




