from django.urls import path

from photo.views import *

urlpatterns = [
    path('', HomePhoto, name='volonterlor'),
    path('media/gallery/', GalleeryList.as_view(), name='gallery_list'),
    path('media/gallery/album/<str:slug>/', ImageList, name='album_detail'),
    path('media/gallery/video/', VideoList.as_view(), name='video_list'),
    path('media/gallery/media/', MediaList.as_view(), name='media_list'),
]
