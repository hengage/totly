from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<slug:slug>/', views.UpdateUserView.as_view(), name='update_user'),
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
    path('signup/', views.CustomSIgnUpView.as_view(), name='account_signup'),
    # allauth 
    path('', include('allauth.urls')),
]