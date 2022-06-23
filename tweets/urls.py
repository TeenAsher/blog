"""Defines URL patterns for tweets"""

from django.urls import path
from . import views

app_name = 'tweets'
urlpatterns = [
    # Home page:
    path('', views.index, name='index'),
    # Page that shows all the blog
    path('posts/', views.posts, name='posts'),
]