from django.urls import path

from news.ru_views import *

urlpatterns = [
    path('', News.as_view(), name='ru_news_list'),
    path('category/news', NewsList.as_view(), name='ru_category'),
    path('category/kairymduuluk', kairymduuluk, name='ru_kairymduuluk'),
    path('category/ofonde/', Ofonde, name='ru_ofonde'),
    path('article/<str:slug>', ArticleDetail.as_view(), name='ru_article_detail'),
    path('user_reaction/', UserReactionView.as_view(), name='ru_user_reaction'),
    path('search/', search, name='ru_search'),
]
