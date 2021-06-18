"""
Entity definitions
"""

from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)


class Author(Model):
    """
    Model corresponding "author" entity

    Attributes
    ----------
    name : string
        Full name of the author
    
    username : string
        Username of the author. Must be unique
    
    email : string
        Email of the author, not necessarily unique
    
    date : datetime
        Automatically adds the current datetime
    """

    name = CharField(max_length=50)
    username = CharField(max_length=50, unique=True)
    email = EmailField(max_length=50)
    date = DateTimeField(auto_now_add=True)


class Article(Model):
    """
    Model corresponding "article" entity

    Attributes
    ----------
    title : string
        Title of the article
    
    author : Author
        Corresponding author who wrote the article

    subject : string
        Subject of the article

    body : string
        Textfield which contains the body of the arrticle
    """

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
        """
        Specify how a model can be identified as unique
        Also how to order them
        """

        unique_together = [
            'author',
            'title',
            'subject',
        ]
        ordering = ['title']
