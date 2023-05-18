from django import forms

from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'description', 'category', 'content',]

        
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'content',]

        
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body',]