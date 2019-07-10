from django.urls import path
from . import views


# add those urls here!!
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('evanpatterson/', views.EvanPageView.as_view(), name='EvanPatterson'),
    path('sethangell/', views.SethPageView.as_view(), name='SethAngell'),
]
