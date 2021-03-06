# users/models.py
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models

class CustomUser(AbstractUser):
    pass
    avatar = models.ImageField(upload_to='media/images/', default='media/images/DefaultProf.jpg')
    slug = models.SlugField(unique=True)
    is_community_member = models.BooleanField("community status", default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)


    def __str__(self):
        return self.username