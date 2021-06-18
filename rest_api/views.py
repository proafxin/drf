"""
Views to be mapped to different endpoints
"""

# Author: Masum Billal

from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
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

    Attributes
    ----------
    queryset : List
        A list of objects that will be used to show the list
    
    serializer_class : Serializer
        The class which will be used to serialize article
        objects to JSON and vice versa
    
    authentication_classes: List
        Specifies which authentication class to use. Here,
        session, token and basic authentications are used
    
    permission_classes : List
        Specifies which permission class to use. Here,
        only authenticated users are permitted.
    """

    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class AuthorList(ListCreateAPIView):
    """
    Generic class based view for list of authors endpoint

    Attributes
    ----------
    queryset : List
        A list of objects that will be used to show the list
    
    serializer_class : Serializer
        The class which will be used to serialize author
        objects to JSON and vice versa
    
    authentication_classes: List
        Specifies which authentication class to use. Here,
        session, token and basic authentications are used
    
    permission_classes : List
        Specifies which permission class to use. Here,
        only authenticated users are permitted.
    """

    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class ArticleDetailGeneric(RetrieveUpdateDestroyAPIView):
    """
    Generic class based view for list author get, put, delete

    Attributes
    ----------
    queryset : List
        A list of objects that will be used to show the list
        Even though a single article will be shown in the page,
        it is still required to pass a list of articles
    
    serializer_class : Serializer
        The class which will be used to serialize article
        objects to JSON and vice versa
    
    authentication_classes: List
        Specifies which authentication class to use. Here,
        session, token and basic authentications are used
    
    permission_classes : List
        Specifies which permission class to use. Here,
        only authenticated users are permitted.
    """

    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class ArticleDetailPost(CreateAPIView):
    """
    Generic class based view for article view by id and create

    Attributes
    ----------
    queryset : List
        A list of objects that will be used to show the list
        Even though a single article will be shown in the page,
        it is still required to pass a list of articles
    
    serializer_class : Serializer
        The class which will be used to serialize article
        objects to JSON and vice versa
    
    authentication_classes: List
        Specifies which authentication class to use. Here,
        session, token and basic authentications are used
    
    permission_classes : List
        Specifies which permission class to use. Here,
        only authenticated users are permitted.
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class AuthorDetailGeneric(RetrieveUpdateDestroyAPIView):
    """
    Generic class based view for author get, put, delete

    Attributes
    ----------
    queryset : List
        A list of objects that will be used to show the list
        Even though a single author will be shown in the page,
        it is still required to pass a list
    
    serializer_class : Serializer
        The class which will be used to serialize author
        objects to JSON and vice versa
    
    authentication_classes: List
        Specifies which authentication class to use. Here,
        session, token and basic authentications are used
    
    permission_classes : List
        Specifies which permission class to use. Here,
        only authenticated users are permitted.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES


class AuthorDetailPost(CreateAPIView):
    """
    Generic class based view for author create and view by id

    Attributes
    ----------
    queryset : List
        A list of objects that will be used to show the list
        Even though a single author will be shown in the page,
        it is still required to pass a list
    
    serializer_class : Serializer
        The class which will be used to serialize article
        object to JSON and vice versa
    
    authentication_classes: List
        Specifies which authentication class to use. Here,
        session, token and basic authentications are used
    
    permission_classes : List
        Specifies which permission class to use. Here,
        only authenticated users are permitted.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = PERMISSION_CLASSES
