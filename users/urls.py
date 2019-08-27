# users/urls.py
from django.urls import path
from .views import SignUpView, CommunitySignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('communitysignup', CommunitySignUpView.as_view(), name='communitysignup')
]