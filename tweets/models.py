from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """One post in the blog"""
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """String representation"""
        text_len = len(self.text[:])
        if text_len <= 200:
            return f'{self.text[:]}'
        else:
            return f'{self.text[:200]}...'


class PrivatePost(models.Model):
    """Post seen only by registered users"""
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """String representation"""
        text_len = len(self.text[:])
        if text_len <= 200:
            return f'{self.text[:]}'
        else:
            return f'{self.text[:200]}...'


class BlogComments(models.Model):
    """A comment under the blog post"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """String representation"""
        return self.text


class PrivateComments(models.Model):
    """A comment under the private post"""
    post = models.ForeignKey(PrivatePost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """String representation"""
        return self.text
