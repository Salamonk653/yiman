# -*- coding: utf-8 -*-
# Create your models here.
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import *

from news.models import *
from photo.models import Image


class News(ListView):
    model = New
    template_name = 'ru/index_1.html'

    def get_context_data(self, *args, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['article'] = New.objects.first()
        context['volonterlor'] = Image.objects.filter(album__name__icontains='Волонтерлор',
                                                       is_public=True).order_by('-id')[:8]
        context['news'] = New.objects.filter(category__name__iexact='Жаңылыктар', language__name__icontains='ru',
                                             is_public=True).order_by('-id')[:4]
        context['fond'] = Fondjonundo.objects.filter(language__name__icontains='ru')
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        index = []
        for i in range(1, context['news'].count() + 1):
            index.append(i)
        context['index'] = index
        context['slider'] = Slider.objects.filter(language__name__icontains='ru')
        context['fon'] = Fon.objects.first()
        context['kairymduuluk'] = Kairymduuluk.objects.filter(language__name__icontains='ru')[:1]
        return context


class NewsList(ListView):
    model = New
    template_name = 'ru/new_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['category'] = New.objects.filter(category__name='Жаңылыктар', language__name__icontains='ru').order_by('-id')
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['fon'] = Fon.objects.first()
        return context


class ArticleDetail(DetailView):
    model = New
    template_name = 'ru/new_list_detail.html'
    category = Category

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['articles'] = self.model.objects.filter(language__name__icontains='ru', is_public=True).order_by('-id')[:15]
        context['article'] = self.get_object()
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['fon'] = Fon.objects.first()
        return context


def kairymduuluk(request):
    context = {}
    context['article'] = Kairymduuluk.objects.filter(language__name__icontains='ru').first()
    context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
    context['fon'] = Fon.objects.first()
    return render(request, 'ru/kairymduuluk.html', context)


def Ofonde(request):
    context = {}
    context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
    context['fond'] = Fondjonundo.objects.filter(language__name__icontains='ru')
    context['fon'] = Fon.objects.first()
    return render(request, 'ru/ofonde.html', context)


class UserReactionView(View):
    template_name = 'ru/new_list_detail.html'

    def get(self, request, *args, **kwargs):
        article_id = self.request.GET.get('article_id')
        article = New.objects.get(id=article_id)
        like = self.request.GET.get('like')
        dislike = self.request.GET.get('dislike')
        if like and (request.user not in article.user_rection.all()):
            article.likes += 1
            article.user_rection.add(request.user)
            article.save()
        if dislike and (request.user not in article.user_rection.all()):
            article.dislikes += 1
            article.user_rection.add(request.user)
            article.save()
        dannyi = {
            'likes': article.likes,
            'dislikes': article.dislikes
        }
        return JsonResponse(dannyi)


from django.shortcuts import render
from .documents import PostDocument


def search(request):
    context = {}
    q = request.GET.get('q')

    if q:
        # context['posts'] = PostDocument.search().query("match", name=q)
        context['posts'] = New.objects.filter(name__icontains=q)
    else:
        context['posts'] = ''

    context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
    context['fon'] = Fon.objects.first()
    return render(request, 'search/search.html', context)
