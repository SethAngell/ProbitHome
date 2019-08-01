from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
from users.models import CustomUser
from django.views.generic import CreateView, UpdateView

def blog_index(request):
    # Index the Post (blog) table and pulls all posts, sorted by newest to oldest
    posts = Post.objects.all().order_by('-created_on')
    # Packages said posts up into a dictionary
    context = {
        "posts": posts,
    }
    # Returns render function which displays the webpage
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    # Filters all post objects for a certain category, and then returns a chronological '<QueryObject>' once again
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

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

    return render(request, "blog_detail.html", context)

def blog_user(request, author):
    # When filtering by another DB object entirely (such as user) make sure that you specify that it should search by string
    desiredUser = CustomUser.objects.get(username=str(author))
    posts = Post.objects.filter(author=desiredUser).order_by('-created_on')
    context = {
        "author": author,
        "posts": posts
    }
    return render(request, "blog_user.html", context)


# Will update with next push
# class blog_create(CreateView):
#     model = Post
#     template = 'blog_create.html'
#     fields = ['title, body, categories, Header']
#
# class blog_edit(UpdateView):
#     model = Post
#     template = 'blog_edit.html'
#     fields = ['title, body, categories, Header']

