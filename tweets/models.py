from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """One post in the blog"""
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
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
    text = models.TextField
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """String representation"""
        text_len = len(self.text[:])
        if text_len <= 200:
            return f'{self.text[:]}'
        else:
            return f'{self.text[:200]}...'
        