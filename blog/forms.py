from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form to leave a comment on the post that is stored the model of Comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)
