from django.shortcuts import render
from django.views.generic import DetailView, ListView
from blog.models import About, Post
from django.core.paginator import Paginator

class BlogPageView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'

class AboutView(ListView):
    model = About
    template_name = 'about.html'