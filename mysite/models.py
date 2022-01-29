from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# from datetime import datetime, date


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='posts-images', blank=False, default='posts-images/post.jpg')
    sumText = models.TextField(max_length=450)
    text = RichTextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    promote = models.BooleanField(default=False)
    views = models.IntegerField(default=0, editable=False)
    commentCount = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return 'Title: ' + self.title + ' | Author: ' + str(self.author)

    def snippet(self):
        return self.sumText[:100] + ' ...'

    def get_absolute_url(self):
        return reverse('posts')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subComment', blank=True, null=True)

    # parent = models.ForeignKey(..., on_delete=models.CASCADE, related_name='subComments')

    def __str__(self):
        return 'Comment by {}'.format(self.name) + ' | Post: ' + self.post.title + ' | Post by ' + str(self.post.author)

    def get_absolute_url(self):
        return reverse('comments')
