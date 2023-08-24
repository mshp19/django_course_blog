from django.shortcuts import reverse
import self as self
from django.db import models


class Post(models.Model):
    objects = None
    status_choices = (
        ('pub', 'published'),
        ('drf', 'draft')

    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status_choices, max_length=3)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.id])














