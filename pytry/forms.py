from django import forms
from .models import Comment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comments"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comments",
            "right",
        ]