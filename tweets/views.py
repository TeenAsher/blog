import http

from django.shortcuts import render, redirect
from .models import BlogPost, PrivatePost, SuperPrivatePost, User
from .forms import BlPostForm, PrPostForm, BlComForm, PrComForm, SupPrPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request):
    """The home page of the Blog"""
    return render(request, 'tweets/index.html')


def posts(request):
    """The page that shows all the blog's posts"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'tweets/posts.html', context)


@login_required
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


@login_required
def priv_com(request, post_id):
    """The page that shows comments under the private post"""
    post = PrivatePost.objects.get(id=post_id)
    comments = post.privatecomments_set.order_by('-date_added')
    context = {'post': post, 'comments': comments}
    return render(request, 'tweets/priv_com.html', context)


@login_required
def new_post(request):
    """Write a new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlPostForm()
    else:
        # POST data submitted; process data
        form = BlPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('tweets:posts')

    context = {'form': form}
    return render(request, 'tweets/new_post.html', context)


@login_required
def new_prpost(request):
    """Write a new private post"""
    if request.method != 'POST':
        form = PrPostForm()
    else:
        form = PrPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('tweets:more')

    context = {'form': form}
    return render(request, 'tweets/new_prpost.html', context)


@login_required
def new_com(request, post_id):
    """Write a new BlogComment"""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        form = BlComForm()
    else:
        form = BlComForm(data=request.POST)
        if form.is_valid():
            new_comm = form.save(commit=False)
            new_comm.post = post
            new_comm.save()
            return redirect('tweets:blog_com', post_id=post_id)

    context = {'post': post, 'form': form}
    return render(request, 'tweets/new_com.html', context)


@login_required
def new_prcom(request, post_id):
    """Write a new PrivateComment"""
    post = PrivatePost.objects.get(id=post_id)

    if request.method != 'POST':
        form = PrComForm()
    else:
        form = PrComForm(data=request.POST)
        if form.is_valid():
            new_comm = form.save(commit=False)
            new_comm.post = post
            new_comm.save()
            return redirect('tweets:priv_com', post_id=post_id)

    context = {'post': post, 'form': form}
    return render(request, 'tweets/new_prcom.html', context)


@login_required
def my_diary(request):
    """Shows user's super private posts"""
    post = SuperPrivatePost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'post': post}
    return render(request, 'tweets/my_diary.html', context)


@login_required
def new_thought(request):
    """Page for writing super private posts"""
    if request.method != 'POST':
        form = SupPrPostForm()
    else:
        form = SupPrPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('tweets:my_diary')

    context = {'form': form}
    return render(request, 'tweets/new_thought.html', context)
