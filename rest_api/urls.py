from django.urls import path

from rest_api.views import (
    article_list,
    AuthorList,
    ArticleList,
)

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='articles'),
    path('authors/', AuthorList.as_view(), name='authors'),
]