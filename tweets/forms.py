from django import forms

from .models import BlogPost, PrivatePost

class BlPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': ''}


class PrPostForm(forms.ModelForm):
    class Meta:
        model = PrivatePost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': ''}

