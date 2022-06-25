from django import forms

from .models import BlogPost

class BlPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
