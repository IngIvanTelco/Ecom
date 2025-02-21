"""
URL configuration for ecomprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
 #   path('', views.index, name='home'),
 #   path('', views.index, name='playlists'),
 #   path('', views.index, name='videos'),
 #   path('', views.index, name='contact'),
 #   path('article/<int:id>/', views.article_detail, name='article_detail'),
 #   path('article/<int:id>/', views.playlist_detail, name='playlist_detail'),
    ## urls deepseek
    path('', views.home, name='home'),  # Home page
    path('playlists/', views.playlists, name='playlists'),  # Playlists page
    path('videos/', views.videos, name='videos'),  # Videos page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('spotify/', views.redirigir_a_spotify, name='redirigir_a_spotify'),  # Redirect to Spotify playlist
]
