from django.conf.urls import url

from photo.ru_views import *

urlpatterns = [
    url(r'^$', HomePhoto, name='ru_volonterlor'),
    url(r'^media/gallery/$', GalleeryList.as_view(), name='ru_gallery_list'),
    url(r'^media/gallery/album/(?P<slug>[\w-]+)/$', ImageList, name='ru_album_detail'),
    url(r'^media/gallery/video/$', VideoList.as_view(), name='ru_video_list'),
    url(r'^media/gallery/media/$', MediaList.as_view(), name='ru_media_list'),
]
