from django.urls import path
from . import views


# add those urls here!!
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
]
