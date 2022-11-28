from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import CustomUser

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):

    # password is a "custom" field on the UserCreationForm, since it does not exist as a model field on the User model. 
    # Meta.widgets will not work for this custom field, so I redefined it's field and widget here.
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = None
            
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new_email = User.objects.filter(email=email)
        if new_email.count():
            raise ValidationError(
                'Email belongs to an existing account, please use another email or login.'
            )
        return email

    def clean_password1(self):
        """
        Check if password has whitespace
        """
        password1 = self.cleaned_data['password1']
        if password1.find(' ') != -1:
            raise ValidationError('Password can\'t contain spaces')
        return password1

    
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'email']
