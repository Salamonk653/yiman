# -*- coding: utf-8 -*-
# Create your models here.
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from django.views.generic import *

from news.models import Fon, OFonde, Slider
from photo.models import *


def HomePhoto(request):
    context = {}
    images = Image.objects.filter(album__name__icontains='Волонтерлор', is_public=True).order_by('-id')
    context['fon'] = Fon.objects.first()
    context['ofonde'] = OFonde.objects.filter(language__name__icontains='kg').first()
    paginator = Paginator(images, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    context['page_obj'] = page
    return render(request, 'volonter.html', context)


class GalleeryList(ListView):
    model = Album
    template_name = 'album_list.html'
    queryset = Album.objects.filter(is_public=True).order_by('-id')
    context_object_name = 'albums'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(GalleeryList, self).get_context_data(**kwargs)
        context['fon'] = Fon.objects.first()
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='kg').first()
        return context


def ImageList(request, slug):
    context = {}
    album = Album.objects.get(slug=slug)
    images = album.image_set.filter(is_public=True).order_by('-id')
    paginator = Paginator(images, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    context['album'] = album
    context['page_obj'] = page
    context['is_paginated'] = page.has_other_pages()
    context['fon'] = Fon.objects.first()
    context['ofonde'] = OFonde.objects.filter(language__name__icontains='kg').first()
    return render(request, 'gallery/album_list.html', context)


class VideoList(ListView):
    model = Video
    template_name = 'video_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(is_public=True).order_by('-id')
        context['fon'] = Fon.objects.first()
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='kg').first()
        return context


class MediaList(ListView):
    model = Media
    template_name = 'media_list.html'
    queryset = Media.objects.filter(is_public=True, language__name__icontains='kg').order_by('-id')
    context_object_name = 'medias'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(MediaList, self).get_context_data(**kwargs)
        context['fon'] = Fon.objects.first()
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='kg').first()
        return context
