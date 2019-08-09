from django.conf.urls import url
from news.views import *

urlpatterns = [
    url(r'^$', News.as_view(), name='news_list'),
    url(r'^category/news$', NewsList.as_view(), name='category'),
    url(r'^category/kairymduuluk$', kairymduuluk, name='kairymduuluk'),
    url(r'^category/ofonde/$', Ofonde, name='ofonde'),
    url(r'^article/(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='article_detail'),
    url(r'^user_reaction/$', UserReactionView.as_view(), name='user_reaction'),
    url(r'^search/$', search, name='search'),
]
