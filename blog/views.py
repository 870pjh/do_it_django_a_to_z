
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    odering = '-pk'

class PostDetail(DetailView):
    model = Post