from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class  Home(ListView):
    model = Post
    template_name = 'index.html'

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


