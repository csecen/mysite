from django import forms
from .models import Comment

# Create a form so that viewer of the site are able to comment on a post -->
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'comment_auth']
