from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
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


class TestIntegration(APITestCase):

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
    
    def test_endpoint_integration(self):
        self.assertTrue(self.client.login(
            username=USERNAME,
            password=PASSWORD,
        ))
        url = reverse('articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        url = reverse('authors')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        url = '/article/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        url = '/author/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        params = {
            'name': 'new author',
            'username': 'new',
            'email': 'new@test.com',
        }
        url = reverse('author-post')
        response = self.client.post(url, data=params)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        params = {
            'title': 'new article',
            'author': 2,
            'subject': 'new subject',
            'body': 'new blah blah',
        }
        url = reverse('article-post')
        response = self.client.post(url, data=params)
        self.assertEqual(response.status_code, HTTP_201_CREATED)