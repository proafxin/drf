from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
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
    IsAuthenticatedOrReadOnly,
)

from rest_api.models import (
    Author,
    Article,
)
from rest_api.model_serializers import (
    AuthorSerializer,
    ArticleSerializer,
)


def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        data = serializer.data
        json_response = JsonResponse(data=data, safe=False)

        return json_response
    
    if request.method == 'POST':
        parser = JSONParser()
        data = parser.parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json_response = JsonResponse(serializer.data, status=201)
        else:
            json_response = JsonResponse(serializer.errors, status=400)
        
        return json_response

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
    ]

class AuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthenticated,
        IsAdminUser,
    ]

class ArticleDetail(APIView):
    
    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)

            return article
        except Article.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        response = Response(serializer.data)

        return response
    
    def post(self, request, pk, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            status = HTTP_201_CREATED
            response = Response(data=data, status=status)
        else:
            status = HTTP_400_BAD_REQUEST
            response = Response(data=serializer.errors, status=status)
        
        return response

class ArticleDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailPost(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer