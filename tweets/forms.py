from django import forms

from .models import BlogPost, PrivatePost, BlogComments, PrivateComments

class BlPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class PrPostForm(forms.ModelForm):
    class Meta:
        model = PrivatePost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class BlComForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ['text']
        labels = {'text': ''}

