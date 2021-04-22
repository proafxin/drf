"""
Route mapping
"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from rest_api.views import (
    AuthorList,
    ArticleList,
    ArticleDetailGeneric,
    ArticleDetailPost,
    AuthorDetailPost,
    AuthorDetailGeneric,
)


urlpatterns = [
    path('articles/', ArticleList.as_view(), name='articles'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('article/<int:pk>', ArticleDetailGeneric.as_view(), name='article'),
    path('article/', ArticleDetailPost.as_view(), name='article-post'),
    path('author/', AuthorDetailPost.as_view(), name='author-post'),
    path('author/<int:pk>', AuthorDetailGeneric.as_view(), name='author-all'),
    path('api_token/', obtain_auth_token),
]
