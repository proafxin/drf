from django.urls import path

from rest_api.views import (
    AuthorList,
    ArticleList,
    ArticleDetail,
    ArticleDetailGeneric,
    ArticleDetailPost,
)

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='articles'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('article/<int:pk>', ArticleDetailGeneric.as_view(), name='article'),
    path('article/', ArticleDetailPost.as_view(), name='article-post'),
]