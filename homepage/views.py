from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class EvanPageView(TemplateView):
    template_name = 'EvanPatterson.html'

class SethPageView(TemplateView):
    template_name = 'SethAngell.html'