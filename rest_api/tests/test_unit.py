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

class TestUnit(APITestCase):
    
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
    
    def check_login(self):
        self.assertTrue(
            self.client.login(
                username=USERNAME,
                password=PASSWORD,
            )
        )
    
    def test_get_article_list(self):
        self.check_login()
        url = 'articles'
        response = self.client.get(reverse(url))
        data = response.json()
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
        for i in range(len(data)):
            self.assertEqual(data[i]['id'], i+1)
            self.assertIsInstance(data[i], dict)
        self.assertEqual(data[2]['title'], 'title big')
        self.assertEqual(data[0]['title'], 'title1')
        self.assertEqual(data[1]['title'], 'title2')
        self.client.logout()
        self.assertFalse(self.client.force_authenticate(user=None))
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
    
    def test_get_article_detail(self):
        self.check_login()
        url = '/article/1'
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['title'], 'title1')
        self.client.logout()
        self.assertFalse(self.client.force_authenticate(user=None))
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, HTTP_200_OK)
    
    def test_post_article_detail(self):
        self.check_login()
        params = {
            "title": "title new",
            "author": 1,
            "subject": "subject new",
            "body": "body new",
        }
        url = reverse('article-post')
        response = self.client.post(url, params)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['author'], 1)
        self.assertEqual(data['id'], 4)
        self.client.logout()
        response = self.client.post(url, params)
        self.assertNotEqual(response.status_code, HTTP_201_CREATED)
    
    def test_get_author_list(self):
        self.check_login()
        url = reverse('authors')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        for i in range(len(data)):
            self.assertIsInstance(data[i], dict)
            self.assertTrue('id' in data[i])
            self.assertEqual(data[i]['id'], i+1)
        self.client.logout()
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, HTTP_200_OK)
    
    def test_get_author_detail(self):
        self.check_login()
        url = '/author/2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertTrue('id' in data)
        self.assertEqual(data['id'], 2)
        self.assertEqual(len(data['articles']), 2)
        for x in data['articles']:
            self.assertIsInstance(x, dict)
            self.assertTrue('author' in x)
            self.assertEqual(x['author'], 2)
        self.client.logout()
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, HTTP_200_OK)
    
    def test_post_author_detail(self):
        self.check_login()
        url = reverse('author-post')
        params = {
            'name': 'test new',
            'username': 'testname4',
            'email': 'test4@test.com',
        }
        response = self.client.post(path=url, data=params)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        data = response.json()
        self.assertTrue('id' in data)
        self.assertEqual(data['id'], 3)
        self.client.logout()
        response = self.client.post(url, params)
        self.assertNotEqual(response.status_code, HTTP_201_CREATED)