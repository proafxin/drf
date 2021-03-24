from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)
from rest_framework.test import APITestCase

from rest_api.models import (
    Author,
    Article,
)

USERNAME = 'abc'
PASSWORD = 'test'

class TestAuthor(APITestCase):
    
    def setUp(self):
        self.user = user = User.objects.create_user(
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
    
    def test_get_article_list(self):
        self.assertTrue(
            self.client.login(
                username=USERNAME,
                password=PASSWORD,
            )
        )
        url = 'articles'
        response = self.client.get(reverse(url))
        data = response.json()
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(data[2]['title'], 'title big')
        self.assertEqual(data[0]['title'], 'title1')
        self.assertEqual(data[1]['title'], 'title2')
        