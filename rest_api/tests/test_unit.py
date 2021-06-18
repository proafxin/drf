"""
Unit test for rest_api
"""

# Author: Masum Billal

from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN,
)
from rest_framework.test import APITestCase

from rest_api.tests.test_integration import (
    create_authors_articles,
    USERNAME,
    PASSWORD,
)


class TestUnit(APITestCase):
    """
    Unit test for author article rest api
    """

    def setUp(self):
        """
        Call function to create authors and articles for this testing
        """

        create_authors_articles()

    def check_login(self):
        """
        Use this method at the start of every test for authentication
        """

        self.assertTrue(
            self.client.login(
                username=USERNAME,
                password=PASSWORD,
            )
        )

    def test_get_article_list(self):
        """
        Unit test for checking list of articles endpoint
        """

        self.check_login()
        url = 'articles'
        response = self.client.get(reverse(url))
        data = response.json()
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
        for i, data_i in enumerate(data):
            self.assertEqual(data_i['id'], i+1)
            self.assertIsInstance(data_i, dict)
        self.assertEqual(data[2]['title'], 'title big')
        self.assertEqual(data[0]['title'], 'title1')
        self.assertEqual(data[1]['title'], 'title2')
        self.client.logout()
        self.assertFalse(self.client.login(
            username=None,
            password=None,
        ))
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_article_detail(self):
        """
        Unit test for checking individual article
        """

        self.check_login()
        url = '/article/1'
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['title'], 'title1')
        self.client.logout()
        self.assertFalse(self.client.login(
            username=None,
            password=None,
        ))
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, HTTP_200_OK)

    def test_post_article_detail(self):
        """
        Unit test for testing article post
        """

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
        """
        Unit test for testing list of authors
        """

        self.check_login()
        url = reverse('authors')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        for i, data_i in enumerate(data):
            self.assertIsInstance(data_i, dict)
            self.assertTrue('id' in data_i)
            self.assertEqual(data_i['id'], i+1)
        self.client.logout()
        self.client.login(
            username=None,
            password=None,
        )
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, HTTP_200_OK)

    def test_get_author_detail(self):
        """
        Unit test for testing individual author
        """

        self.check_login()
        url = '/author/2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertTrue('id' in data)
        self.assertEqual(data['id'], 2)
        self.assertEqual(len(data['articles']), 2)
        for data_i in data['articles']:
            self.assertIsInstance(data_i, dict)
            self.assertTrue('author' in data_i)
            self.assertEqual(data_i['author'], 2)
        self.client.logout()
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, HTTP_200_OK)

    def test_post_author_detail(self):
        """
        Unit test for testing author creation
        """

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
