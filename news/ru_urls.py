# -*- coding: utf-8 -*-
# Create your models here.
from django.conf.urls import url

from news.ru_views import *

urlpatterns = [
    url(r'^$', News.as_view(), name='ru_news_list'),
    url(r'^category/news/$', NewsList.as_view(), name='ru_category'),
    url(r'^category/kairymduuluk/$', kairymduuluk, name='ru_kairymduuluk'),
    url(r'^category/ofonde/$', Ofonde, name='ru_ofonde'),
    url(r'^article/(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='ru_article_detail'),
    url(r'^user_reaction/$', UserReactionView.as_view(), name='ru_user_reaction'),
    url(r'^search/$', search, name='ru_search'),
]
