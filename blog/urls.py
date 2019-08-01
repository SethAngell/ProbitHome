from django.urls import path
from . import views
#from .views import blog_create, blog_edit

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    path("user/<author>/", views.blog_user, name="blog_user"),
    # path("<int:pk>/edit", blog_edit.as_view(), name="blog_edit"),
    # path("new/", blog_create.as_view(), name="blog_new")
]