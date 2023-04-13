from django.urls import path, include

from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('posts/create/', views.CreatePostView.as_view(), name='create_post'),
   path('posts/<slug:slug>/', views.PostDetailView, name='post_detail'),
   path('posts/<slug:slug>/update/', views.UpdatePostView.as_view(), name='update_post'),
   path('posts/<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
   path('search/', views.SearchView.as_view(), name='search'),
   path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category'),
    path('load_more_comments/', views.load_more_comments, name='load_more_comments'),
   path('comments/<int:pk>/delete/', views.DeleteCommentView.as_view(), name='delete_comment'),

   # Django prose Richtext editor
   path("prose/", include("prose.urls")),
]
