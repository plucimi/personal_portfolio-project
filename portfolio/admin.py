from django.contrib import admin
from .models import Project
from blog.models import Blog_post

admin.site.register(Project)
admin.site.register(Blog_post)