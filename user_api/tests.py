from django.test import TestCase
import json
from .models import User, Card
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class UserRegisterTests(APITestCase):
    def test_registration(self):
        data = {
            "username": "test1",
            "phone": "+996704375000",
            "email": "test1@test1.com",
            "password": "kanat2002",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTests(APITestCase):
    url = reverse("profile_api")

    def setUp(self):
        self.user = User.objects.create_user(
            phone="+996704375003",
            password="kanat2002",
            username="testtest1",
            email="tester@test.com",
        )
        self.user.save()
        self.token = self.client.get(
            reverse("token_obtain"),
            data={"phone": "+996704375003", "password": "kanat2002"},
        )

    def api_authentication(self):
        self.client.crendentionals(HTTP_AUTHORIZTION="JWT " + self.token)

    def test_profile_autheticated(self):
        response = self.client.get(self.url, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# Create your tests here.
