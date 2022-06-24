from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    return render(request, 'index.html',{})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


