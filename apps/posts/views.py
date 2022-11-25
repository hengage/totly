from django.views import generic
from django.views.generic import edit
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Post
from .forms import CreatePostForm
class HomeView(generic.ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'post_list'
    paginate_by = 6

class CreatePostView(edit.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def PostDetailView(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)

    context = {
        'post':post,
        }
    template = 'posts/post_detail.html'
    return render(request, template, context)