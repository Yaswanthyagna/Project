from django.shortcuts import render
from pytube import YouTube
import pytube
from django.http import HttpResponse
from embeddify import Embedder

# Create your views here.


def home(request):

    return render(request, 'pages/home.html')


def ytb_down(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        var = Embedder()
        video.download()
        context = {"link": var(url)}
        return render(request, 'pages/home.html', context)
    return render(request, 'pages/home.html')
