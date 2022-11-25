from django.urls import path

from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('posts/create', views.CreatePostView.as_view(), name='create_post'),
]
