"""
Serializer of the models for exposing to rest api
"""

from rest_framework.serializers import (
    ModelSerializer,
)

from rest_api.models import (
    Article,
    Author,
)


class ArticleSerializer(ModelSerializer):
    """
    Serializer for the model Article. Use ModelSerializer instead of the usual Serializer
    """

    class Meta:
        """
        Specify the model for which the serializer is built
        Also specify which fields should be used for serialization
        If you want to use all fields, use __all__ instead of specifying
        every field manually
        """

        model = Article
        fields = [
            'id',
            'title',
            'author',
            'subject',
            'body',
        ]


class AuthorSerializer(ModelSerializer):
    """
    Model serializer for the model Author
    """

    articles = ArticleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        """
        Specify that this serializer is for Author model
        """

        model = Author
        fields = [
            'id',
            'name',
            'username',
            'email',
            'articles',
        ]
