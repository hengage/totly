from django.views import generic
from .models import Post
class HomeView(generic.ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'post_list'
    paginate_by = 6