from django.db.models import (
    Model,
    CharField,
    AutoField,
    EmailField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)

class Author(Model):
    #author_id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    username = CharField(max_length=50, unique=True)
    email = EmailField(max_length=50)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(Model):
    #article_id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    author = ForeignKey(
        Author,
        on_delete=CASCADE,
        null=False,
        related_name='articles',
    )
    subject = CharField(max_length=100)
    body = CharField(max_length=500)

    class Meta:
        unique_together = [
            'author',
            'title',
            'subject',
        ]
        ordering = ['title']
    
    def __str__(self):
        return self.title