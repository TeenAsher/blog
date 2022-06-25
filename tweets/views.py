from django.shortcuts import render, redirect
from .models import BlogPost, PrivatePost, BlogComments, PrivateComments
from .forms import BlPostForm
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


def priv_com(request, post_id):
    """The page that shows comments under the private post"""
    post = PrivatePost.objects.get(id=post_id)
    comments = post.privatecomments_set.order_by('-date_added')
    context = {'post': post, 'comments': comments}
    return render(request, 'tweets/priv_com.html', context)


def new_post(request):
    """Write a new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlPostForm()
    else:
        # POST data submitted; process data
        form = BlPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweets:posts')

    context = {'form': form}
    return render(request, 'tweets/new_post.html', context)