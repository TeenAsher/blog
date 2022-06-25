from django.shortcuts import render
from .models import BlogPost, PrivatePost, BlogComments, PrivateComments
# Create your views here.
def index(request):
    """The home page of the Blog"""
    return render(request, 'tweets/index.html')


def posts(request):
    """The page that shows all the blog's posts"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'tweets/posts.html', context)


def more(request):
    """The page that shows private posts"""
    post = PrivatePost.objects.order_by('-date_added')
    context = {'post': post}
    return render(request, 'tweets/more.html', context)


def blog_com(request, post_id):
    """The page that shows comments under the post"""
    post = BlogPost.objects.get(id=post_id)
    comments = post.blogcomments_set.order_by('-date_added')
    context = {'post': post, 'comments': comments}
    return render(request, 'tweets/blog_com.html', context)
