from django.http import (
    HttpResponse,
    JsonResponse,
)

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.status import (
#     HTTP_200_OK,
#     HTTP_201_CREATED,
#     HTTP_400_BAD_REQUEST,
# )
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)

from rest_api.models import (
    Author,
    Article,
)
from rest_api.model_serializers import (
    AuthorSerializer,
    ArticleSerializer,
)

AUTHENTICATION_CLASSES = [
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
]
PERMISSION_CLASSES = [IsAuthenticated]


class ArticleList(ListCreateAPIView):
    """
    Generic class based view for list of articles endpoint
    """

    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class AuthorList(ListCreateAPIView):
    """
    Generic class based view for list of authors endpoint
    """

    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class ArticleDetailGeneric(RetrieveUpdateDestroyAPIView):
    """
    Generic class based view for list author get, put, delete
    """

    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class ArticleDetailPost(CreateAPIView):
    """
    Generic class based view for article view by id and create
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class AuthorDetailGeneric(RetrieveUpdateDestroyAPIView):
    """
    Generic class based view for author get, put, delete
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class AuthorDetailPost(CreateAPIView):
    """
    Generic class based view for author create and view by id
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES