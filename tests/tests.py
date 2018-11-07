from django.test import TestCase, SimpleTestCase, TransactionTestCase
from api import models
from rest_framework.test import APIClient
from rest_framework import status

# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class MyTestCaseBase(TestCase):
    testUserUsername = "test"
    testUserPassword = "test"
    testUserEmail = "test@test.com"

    def setUp(self):
        self.client = APIClient()
        models.WobblyUser.objects.create_user(self.testUserUsername,self.testUserEmail, self.testUserPassword)
        self.client.login(username=self.testUserUsername, password=self.testUserPassword)
    def tearDown(self):
        self.client.logout()

class RootEndpointTestCase(MyTestCaseBase):
    def test_list_response(self):
        response = self.client.get('/')
        assert response.status_code == status.HTTP_200_OK

class SwaggerRootEndpointTestCase(MyTestCaseBase):
    def test_response(self):
        response = self.client.get('/swagger/')
        assert response.status_code == status.HTTP_200_OK

class DocsEndpointTestCase(MyTestCaseBase):
    def test_response(self):
        response = self.client.get('/docs/')
        assert response.status_code == status.HTTP_200_OK

class SchemaEndpointTestCase(MyTestCaseBase):
    def test_list_response(self):
        response = self.client.get('/schema/')
        assert response.status_code == status.HTTP_200_OK