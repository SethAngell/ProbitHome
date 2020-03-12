from django.urls import path
from .views import blog_index, blog_category, blog_user, blog_new, blog_edit
from . import views
#from .views import blog_create, blog_edit

urlpatterns = [
    path("", blog_index.as_view(), name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", blog_category.as_view(), name="blog_category"),
    path("user/<author>/", blog_user.as_view(), name="blog_user"),
    path("post/new/", views.blog_new, name="blog_new"),
    path('<int:pk>/edit/', blog_edit.as_view(), name='blog_edit'),
]