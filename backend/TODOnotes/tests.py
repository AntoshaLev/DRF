from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, \
    force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from .models import ToDo
from .views import UserModelViewSet, ToDoModelViewSet, ProjectModelViewSet
from mixer.backend.django import mixer


class TestUserApi(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        admin = User.objects.create_superuser(
            username='admin',
            email='test@mail.com',
            password='qwerty'
        )
        request = factory.get('/api/users')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_list_with_data(self):
        User.objects.create_user(
            username='test',
            email='some@mail.com',
            password='123'
        )
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(len(response.data), 1)

    def test_get_list_client(self):
        admin = User.objects.create_superuser(
            'admin',
            email='test@mail.com',
            password='qwerty'
        )
        client = APIClient()
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(len(response.data), 1)


class TestUserClientApi(APITestCase):
    def setUp(self) -> None:
        self.admin = User.objects.create_superuser(
            'admin',
            email='test@mail.com',
            password='qwerty'
        )
        self.user = User.objects.create_user(
            username='test',
            email='some@mail.com',
            password='123'
        )
        self.todo = mixer.blend(
            ToDo,
            todo_text='Do something'
        )

    def test_get_list_client_test_case(self):
        self.client.login(username='admin', password='qwerty')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_list_403(self):
        self.client.login(username='admin', password='qwerty')
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)