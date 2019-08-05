from django.urls import path
from django.contrib.auth import views as auth_views
from news.views import *

urlpatterns = [
    path('', News.as_view(), name='news_list'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('category/news', NewsList.as_view(), name='category'),
    path('category/kairymduuluk', kairymduuluk, name='kairymduuluk'),
    path('category/ofonde/', Ofonde, name='ofonde'),
    path('article/<str:slug>', ArticleDetail.as_view(), name='article_detail'),
    path('user_reaction/', UserReactionView.as_view(), name='user_reaction'),
    path('search/', search, name='search'),
]
