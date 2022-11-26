from django.views import generic
from django.views.generic import edit
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

from .models import Post, Category, Comment
from .forms import CreatePostForm, UpdatePostForm, AddCommentForm

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
    comments = Comment.objects.filter(
        post=post.id
        ).order_by('-id')

    comment_form = AddCommentForm(request.POST or None)
    if comment_form.is_valid():
        content = request.POST.get('comment_body')
        comment = Comment.objects.create(
            post=post,
            commentator=request.user,
            comment_body=content
            )
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = AddCommentForm

    context = {
        'post':post,
        'comments':comments,
        'comment_form':comment_form,
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

class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'posts/category.html'

    def get_context_data(self, *args, **kwargs):
        '''
        Get the posts related to each category
        '''
        category_slug  = self.kwargs['slug'].replace('-', ' ')
        categoryposts = Post.objects.select_related().filter(
            category__category_name__iexact=category_slug
            )
        context = super().get_context_data(*args, **kwargs)
        context['categoryposts'] = categoryposts
        return context