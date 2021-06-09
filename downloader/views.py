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
        adress = request.POST.get('adress')
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        var = Embedder()
        global file_size
        file_size = video.filesize
        context = {"link": var(url), "title": youtube.title,
                   "completed": "Your  video has been downloaded"}
        video.download(adress)
        return render(request, 'pages/home.html', context)
    return render(request, 'pages/home.html')
