from django.urls import path, include

from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('posts/create/', views.CreatePostView.as_view(), name='create_post'),
   path('posts/<slug:slug>/', views.PostDetailView, name='post_detail'),
   path('posts/<slug:slug>/update/', views.UpdatePostView.as_view(), name='update_post'),
   path('posts/<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
   path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category'),

   # Django prose Richtext editor
   path("prose/", include("prose.urls")),
]
