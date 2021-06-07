from downloader.views import home
from django.urls import path





from . import views
urlpatterns = [
    #path('',views.home),
    path('', views.ytb_down, name='home'),
]   