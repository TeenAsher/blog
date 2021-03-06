from django import forms

from .models import BlogPost, PrivatePost, BlogComments, PrivateComments, SuperPrivatePost

class BlPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Write here your thoughts...'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}



class PrPostForm(forms.ModelForm):
    class Meta:
        model = PrivatePost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Don\'t be shy, characters\'re unlimited!'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class BlComForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ['text']
        labels = {'text': 'Type...'}


class PrComForm(forms.ModelForm):
    class Meta:
        model = PrivateComments
        fields = ['text']
        labels = {'text': 'Type...'}


class SupPrPostForm(forms.ModelForm):
    class Meta:
        model = SuperPrivatePost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Dear Diary, ...'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
