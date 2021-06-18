"""
Helper module for testing
"""

# Author: Masum Billal

from django.contrib.auth.models import User

from rest_api.models import (
    Author,
    Article,
)

USERNAME = 'newuser'
PASSWORD = 'password'

def create_authors_articles():
    """
    Create user, authors and articles for test database
    """

    User.objects.create_user(
        username=USERNAME,
        password=PASSWORD,
        email='abc@abc.com',
    )
    author1 = Author.objects.create(
        name='test',
        username='testname',
        email='test@test.com',
    )
    author2 = Author.objects.create(
        name='test2',
        username='testname2',
        email='test2@test.com',
    )
    Article.objects.create(
        author=author1,
        title='title1',
        subject='subject1',
        body='body1',
    )
    Article.objects.create(
        title='title2',
        author=author2,
        subject='subject2',
        body='body2',
    )
    Article.objects.create(
        title='title big',
        author=author2,
        subject='subject big',
        body='body big',
    )