from rest_framework.serializers import (
    ModelSerializer,
)

from rest_api.models import (
    Article,
    Author,
)

class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'author',
            'subject',
            'body',
        ]

class AuthorSerializer(ModelSerializer):
    articles = ArticleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'username',
            'email',
            'articles',
        ]
