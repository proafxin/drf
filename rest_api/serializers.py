# from rest_framework.serializers import (
#     Serializer,
#     CharField,
#     EmailField,
#     DateTimeField,
# )

# from rest_api.models import (
#     Author,
#     Article,
# )

# class ArticleSerializer(Serializer):
#     title = CharField(max_length=100)
#     subject = CharField(max_length=100)
#     body = CharField(max_length=500)

#     def create(self, data_valid):
#         return Article.objects.create(data_valid)
    
#     def update(self, instance, data_new):
#         instance.title = data_new.get('title', instance.title)
#         instance.subject = data_new.get('subject', instance.subject)
#         instance.body = data_new.get('body', instance.body)

# class AuthorSerializer(Serializer):
#     name = CharField(max_length=50)
#     username = CharField(max_length=50)
#     email = EmailField(max_length=50)
#     date = DateTimeField()
#     articles = ArticleSerializer(
#         many=True,
#         read_only=True,
#     )

#     def create(self, data_valid):
#         return Author.objects.create(data_valid)
    
#     def update(self, instance, data_new):
#         instance.name = data_new.get('name', instance.name)
#         instance.username = data_new.get('username', instance.username)
#         instance.email = data_new.get('email', instance.email)
#         instance.date = data_new.get('date', instance.date)
#         instance.articles = data_new.get('articles', instance.articles)
#         instance.save()

#         return instance