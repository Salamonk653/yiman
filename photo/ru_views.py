# -*- coding: utf-8 -*-
# Create your models here.
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from django.views.generic import *

from news.models import Fon, OFonde
from photo.models import *


def HomePhoto(request):
    context = {}
    images = Image.objects.filter(album__name__icontains='Волонтерлор', is_public=True).order_by('-id')
    context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
    context['fon'] = Fon.objects.first()
    paginator = Paginator(images, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context['page_obj'] = page
    return render(request, 'ru/volonter.html', context)


class GalleeryList(ListView):
    model = Album
    template_name = 'ru/album_list.html'
    queryset = Album.objects.filter(is_public=True).order_by('-id')
    context_object_name = 'albums'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(GalleeryList, self).get_context_data(**kwargs)
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['fon'] = Fon.objects.first()
        return context


def ImageList(request, slug):
    context = {}
    album = Album.objects.get(slug=slug)
    images = album.image_set.filter(is_public=True).order_by('-id')
    paginator = Paginator(images, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context['album'] = album
    context['page_obj'] = page
    context['is_paginated'] = page.has_other_pages()
    context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
    context['fon'] = Fon.objects.first()
    return render(request, 'ru/gallery/album_list.html', context)


class VideoList(ListView):
    model = Video
    template_name = 'ru/video_list.html'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(is_public=True).order_by('-id')
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['fon'] = Fon.objects.first()
        return context


class MediaList(ListView):
    model = Media
    template_name = 'ru/media_list.html'
    queryset = Media.objects.filter(is_public=True, language__name__icontains='ru').order_by('-id')
    context_object_name = 'medias'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(MediaList, self).get_context_data(**kwargs)
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['fon'] = Fon.objects.first()
        return context