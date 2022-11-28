from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<slug:slug>/', views.UpdateUserView.as_view(), name='update_user'),

    # allauth 
    path('', include('allauth.urls')),
]