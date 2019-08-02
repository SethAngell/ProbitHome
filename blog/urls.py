from django.urls import path
from . import views
#from .views import blog_create, blog_edit

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    path("user/<author>/", views.blog_user, name="blog_user"),
    path("post/new/", views.blog_new, name="blog_new"),
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
]