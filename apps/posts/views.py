from django.views import generic
from django.views.generic import edit
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Post
from .forms import CreatePostForm, UpdatePostForm

def error_404(request, exception):
    return render(request, 'error_404.html')
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

class UpdatePostView(UserPassesTestMixin, edit.UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'posts/update_post.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeletePostView(UserPassesTestMixin, edit.DeleteView):
    model = Post
    success_url = reverse_lazy('home')
   
    def test_func(self):
        '''
        Forbid a user from editing and deleting posts they
        did not create.
        '''
        obj = self.get_object()
        return obj.author == self.request.user