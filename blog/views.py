from django.shortcuts import render
from blog.models import Configuracion
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post

def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog/index.html', {'configuracion': configuracion} )

class ListPost(ListView):
    model=Post

class CreatePost(CreateView):
    model=Post
    fields = ['title', 'short_content', 'content']
    success_url = reverse_lazy("list-post")

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields=['title', 'short_content', 'content']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)