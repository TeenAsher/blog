from django.contrib import admin
from .models import BlogPost, PrivatePost, BlogComments
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(PrivatePost)
admin.site.register(BlogComments)