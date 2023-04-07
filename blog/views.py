from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class Blog(ListView):
    model = BlogPostModel
    template_name = 'blog/home.html'
    context_object_name = 'blog_item'


class Details(DetailView):
    model = BlogPostModel
    template_name = 'blog/detail.html'
    context_object_name = 'blog_item'
# ^
# |
# def detail(request, pk):
#     blog = get_object_or_404(BlogPostModel, pk=pk)
#     return render(request, 'blog/detail.html', {"blog_item":blog})