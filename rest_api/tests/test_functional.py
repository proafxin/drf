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
from rest_framework.test import RequestsClient
from requests import (
    get,
    post,
)
from requests.auth import HTTPBasicAuth
from json import loads

from rest_api.models import (
    Author,
    Article,
)

IP = '127.0.0.1'
PORT = 8000
USERNAME = 'newuser'
PASSWORD = 'newpassword'
URL = 'http://{}:{}'.format(IP, PORT)
auth_invalid = HTTPBasicAuth(username='wrong', password='wrong')

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
    
    def get_request_client(self):
        client = RequestsClient()
        client.auth = HTTPBasicAuth(USERNAME, PASSWORD)
        client.headers.update({
            'x-test': 'true',
        })

        return client
    
    # def get_user_token(self):
    #     url = URL+'/api-auth-token/'
    #     client = self.get_request_client()
    #     params = {
    #         'username': USERNAME,
    #         'password': PASSWORD,
    #     }
    #     response = client.post(url, data=params)
    #     data = response.content.decode()
    #     data = loads(data)
    #     token = 'Token '+data['token']
    #     params = {
    #         'Authorization': token,
    #     }
    #     response = self.client.get('/articles/', data=params)
    #     self.assertEqual(response.status_code, HTTP_200_OK)
        
    def test_get_article_list(self):
        client = self.get_request_client()
        response = client.get(URL+'/articles/')
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
        for i in range(len(data)):
            self.assertTrue('id' in data[i])
            self.assertEqual(data[i]['id'], i+1)
            self.assertIsInstance(data[i], dict)
    
    def test_get_article_detail(self):
        client = self.get_request_client()
        response = client.get(URL+'/article/1')
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], 1)

    def test_post_article_detail(self):
        client = self.get_request_client()
        params = {
            'title': 'new article',
            'author': 2,
            'subject': 'new subject',
            'body': 'new blah blah',
        }
        response = client.post(URL+'/article/', data=params)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        data = response.json()
        self.assertTrue('id' in data)
        self.assertEqual(data['id'], 4)
    
    def test_get_author_list(self):
        client = self.get_request_client()
        response = client.get(URL+'/authors/')
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        for i in range(len(data)):
            self.assertTrue('id' in data[i])
            self.assertEqual(data[i]['id'], i+1)
            self.assertIsInstance(data[i], dict)
    
    def test_get_author_detail(self):
        client = self.get_request_client()
        response = client.get(URL+'/author/1')
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertTrue('id' in data)
        self.assertEqual(data['id'], 1)
        self.assertTrue('articles' in data)
        for x in data['articles']:
            self.assertIsInstance(x, dict)
            self.assertTrue('author' in x)
            self.assertEqual(x['author'], 1)
    
    def test_post_author_detail(self):
        client = self.get_request_client()
        params = {
            'name': 'new author',
            'username': 'new',
            'email': 'new@test.com',
        }
        response = client.post(URL+'/author/', data=params)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        data = response.json()
        self.assertTrue('id' in data)
        self.assertEqual(data['id'], 3)