from django.views.generic import UpdateView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from allauth.account.views import LoginView, SignupView

from .forms import UpdateUserForm
from posts.views import CategoriesListViewMixin

User = get_user_model()


class CustomLoginView(CategoriesListViewMixin, LoginView):
    pass


class CustomSIgnUpView(CategoriesListViewMixin, SignupView):
    pass


class UpdateUserView(
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    form_class = UpdateUserForm
    model = User
    context_object_name = 'current_user'
    template_name = 'account/update_user.html'
    success_message = 'Hello %(first_name)s Details changed successfully!'

    def get_success_url(self):
        return reverse('update_user', kwargs={'slug': self.get_object().slug})

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
