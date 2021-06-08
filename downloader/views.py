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
        youtube = pytube.YouTube(url,on_progress_callback=progress_Check)
        video = youtube.streams.get_highest_resolution()
        var = Embedder()
        global file_size
        file_size = video.filesize
        context = {"link": var(url),"title":youtube.title,"completed":"Your  video has been downloaded"}  
        video.download()
        return render(request, 'pages/home.html', context)
    return render(request, 'pages/home.html')


def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print("{:00.0f}%  downloaded".format(percent))
