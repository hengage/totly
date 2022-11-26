from django import forms

from .models import Post, Comment

class CreatePostForm(forms.ModelForm):

    class Meta: 
        model = Post
        fields = ['title', 'description', 'content',]
    
        widgets ={
               'title': forms.TextInput(),

               'description': forms.TextInput(),

               'author': forms.TextInput(attrs={'type':'hidden'}),

               'content': forms.Textarea(attrs={'rows': 18}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'content',]

        widgets ={
               'title': forms.TextInput(),

               'description': forms.TextInput(),

               'content': forms.Textarea(attrs={'rows': 18}),
        }

    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body',]

        widgets = {
            'comment_body': forms.Textarea(attrs={'rows': 18})
        }