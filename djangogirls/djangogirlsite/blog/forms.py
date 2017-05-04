from django import forms

from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text', )

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text', )