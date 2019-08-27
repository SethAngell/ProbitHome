from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm
from django import forms
from users.models import CustomUser
from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class blog_index(generic.ListView):
    # Index the Post (blog) table and pulls all posts, sorted by newest to oldest
    queryset = Post.objects.all().order_by('-created_on')
    # Packages said posts up into a dictionary
    template_name = 'blog/blog_index.html'


class blog_category(generic.ListView):
    template_name = "blog/blog_category.html"

    def get_queryset(self):
        user_category = self.kwargs['category']
        print(user_category)
        return Post.objects.filter(categories__name__contains=user_category).order_by('-created_on')

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # Creates a new variable that hold the commenting form
    form = CommentForm()

    # Constantly watches the page to see if there has been any input into the commenting box and then saves it as so
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    # An alternate way to specify which object to filter by
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/blog_detail.html", context)


class blog_user(generic.ListView):
    template_name = 'blog/blog_user.html'

    def get_queryset(self):
        desiredUser = self.kwargs['author']
        user_object = CustomUser.objects.get(username=str(desiredUser))
        return Post.objects.filter(author=user_object).order_by('-created_on')

# REturn to this tomorrow https://stackoverflow.com/questions/42481287/automatically-set-logged-in-user-as-the-author-in-django-using-createview-and-mo
class blog_new(generic.FormView, LoginRequiredMixin):
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

    form_class = PostForm
    template_name = 'blog/blog_edit.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

class blog_edit(generic.UpdateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'body', 'categories', 'Header']
    template_name = 'blog/blog_edit.html'

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)




