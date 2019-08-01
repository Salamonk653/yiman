from django.urls import path

from photo.ru_views import *

urlpatterns = [
    path('', HomePhoto, name='ru_volonterlor'),
    path('media/gallery/', GalleeryList.as_view(), name='ru_gallery_list'),
    path('media/gallery/album/<str:slug>/', ImageList, name='ru_album_detail'),
    path('media/gallery/video/', VideoList.as_view(), name='ru_video_list'),
    path('media/gallery/media/', MediaList.as_view(), name='ru_media_list'),
]
