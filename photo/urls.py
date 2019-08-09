from django.conf.urls import url

from photo.views import *

urlpatterns = [
    url(r'^$', HomePhoto, name='volonterlor'),
    url(r'^media/gallery/$', GalleeryList.as_view(), name='gallery_list'),
    url(r'^media/gallery/album/(?P<slug>[\w-]+)/$', ImageList, name='album_detail'),
    url(r'^media/gallery/video/$', VideoList.as_view(), name='video_list'),
    url(r'^media/gallery/media/$', MediaList.as_view(), name='media_list'),
]
