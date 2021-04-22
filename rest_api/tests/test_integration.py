"""
Integration test for rest_api
"""

from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from rest_framework.test import APITestCase

from rest_api.tests.main import (
    create_authors_articles,
    USERNAME,
    PASSWORD,
)


class TestIntegration(APITestCase):
    """
    Integration test for author/article rest api
    """

    def setUp(self):
        """
        Call function to create authors and articles
        """
        create_authors_articles()

    def test_endpoint_integration(self):
        """
        Test all the endpoints in this method
        to see if any API breaks another
        """

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
