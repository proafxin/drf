from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from django.urls import reverse
from requests import (
    get,
    post,
)

USERNAME = 'masum'
PASSWORD = 'abcdef123'

class FunctionalTest(APITestCase):

    def setUp(self):
        pass

    def test_token(self):
        url = 'http://127.0.0.1:8000/api_token/'
        params = {
            'username': USERNAME,
            'password': PASSWORD,
        }
        response = post(
            url=url,
            data=params,
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertTrue('token' in data)
        token = data['token']
        self.assertIsInstance(token, str)
        token = 'Token '+token
        url = 'http://127.0.0.1:8000/authors/'
        params = {
            'Authorization': token,
        }
        response = get(
            url=url,
            headers=params,
        )
        self.assertEqual(response.status_code, HTTP_200_OK)