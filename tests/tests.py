from django.test import TestCase, SimpleTestCase, TransactionTestCase
from apiv1 import models
from rest_framework.test import APIClient
from rest_framework import status

# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class RootEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_response(self):
        response = self.client.get('/')
        assert response.status_code == status.HTTP_200_OK

class SwaggerRootEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/swagger/')
        assert response.status_code == status.HTTP_200_OK

class DocsEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/docs/')
        assert response.status_code == status.HTTP_200_OK

class SchemaEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_response(self):
        response = self.client.get('/schema/')
        assert response.status_code == status.HTTP_200_OK