# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CommunityUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CommunitySignUpView(CreateView):
    form_class = CommunityUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/community_signup.html'



