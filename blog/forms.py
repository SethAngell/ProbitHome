from django import forms
from .models import Post, Comment


class CommentForm(forms.Form):

    class Meta:
        model = Comment
        author = forms.CharField(max_length=200)
        body = forms.Textarea()


class PostForm(forms.Form):

    class Meta:
        model = Post
        title = forms.CharField(max_length=250)
        body = forms.Textarea()
        header = forms.ImageField()

