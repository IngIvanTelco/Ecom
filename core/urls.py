from django.urls import path
from core.views import index
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index),
     ## urls deepseek
    path('', views.home, name='home'),  # Home page
    path('playlists/', views.playlists, name='playlists'),  # Playlists page
    path('videos/', views.videos, name='videos'),  # Videos page
    path('contact/', views.contact, name='contact'),  # Contact page
]