"""Defines URL patterns for tweets"""

from django.urls import path
from . import views

app_name = 'tweets'
urlpatterns = [
    # Home page:
    path('', views.index, name='index'),
    # Page that shows average posts
    path('posts/', views.posts, name='posts'),
    # Page that shows private posts
    path('more/', views.more, name='more'),
    # Page for reading comments under the average posts
    path('posts/<int:post_id>/', views.blog_com, name='blog_com'),
    # Page for reading comments under the private posts
    path('more/<int:post_id>/', views.priv_com, name='priv_com'),
]