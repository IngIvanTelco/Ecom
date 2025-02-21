from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'core/index.html') # Add this line to the index view
#def article_detail(request, id):
    # Your logic to fetch and display the article
#    return render(request, 'core/article_detail.html', {'id': id})
#def playlist_detail(request, id):
    # Your logic to fetch and display the article
#    return render(request, 'core/playlist_detail.html', {'id': id})

## urls deepseek
def home(request):
    return render(request, 'home.html')  # Render home.html

def playlists(request):
    return render(request, 'playlists.html')  # Render playlists.html

def videos(request):
    return render(request, 'videos.html')  # Render videos.html

def contact(request):
    return render(request, 'contact.html')  # Render contact.html

def redirigir_a_spotify(request):
    return redirect('https://open.spotify.com/playlist/14Ko4z5nl0RlRBrsbtkvHn') # Redirect to Spotify playlist