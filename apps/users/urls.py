from django.urls import path
from . import views

urlpatterns = [
    path('profile/<slug:slug>/', views.UpdateUserView.as_view(), name='update_user'),
]