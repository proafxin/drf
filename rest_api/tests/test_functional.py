"""
Functional test for rest_api
"""

from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from requests import (
    get,
    post,
)

USERNAME = 'masum'
PASSWORD = 'abcdef123'


class FunctionalTest(APITestCase):
    """
    Functional test for author article rest api

    Methods
    -------
    setUp()
        Use this method to declare anything you need for testing

    test_token()
        Functional test to see if token creation properly works
    """

    def setUp(self):
        pass

    def test_token(self):
        """
        Retrieve the token for a particular user using a post request
        Then use this token to authenticate that user

        Tests the endpoint:
            POST /api_token/
        
        Endpoint Parameters
        -------------------
            username : string
                Username of a valid user

            password : string
                Password of the same valid user

        Returns
        -------
        token : string
            Token of the validated user
        """

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
