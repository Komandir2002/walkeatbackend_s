from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Fit
# from user_api import models as users


class FitCreateTests(APITestCase):
    def setUp(self):
        data = Fit.objects.create(
            photo="media/food.svg",
            title="test1",
            carbohydrates=0.0,
            protein=0.0,
            fats=0.0,
            price=0.0,
            ingredients="test test",
            calories=0.0,
            kcal=0.0,
        )
        data.save()

    def test_fit_post_method(self):
        pass


class FitListTests(APITestCase):
    def setUp(self):
        data = Fit.objects.create(
            photo="media/food.svg",
            title="test1",
            carbohydrates=0.0,
            protein=0.0,
            fats=0.0,
            price=0.0,
            ingredients="test test",
            calories=0.0,
            kcal=0.0,
        )
        data.save()

        self.user = users.User.objects.create_user(
            username="testuser",
            phone="+996704375003",
            email="tester@mail.com",
            password="123",
        )
        self.client.force_authenticate(self.user)

    def test_fit_list(self):

        response = self.client.get(reverse("detail_fit_api"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_fit_post(self):
    #     response = self.client.post(reverse("detail_fit_api"), headers="")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ShortFitTest(APITestCase):
    url = reverse("main_menu_api")

    def setUp(self):
        data = Fit.objects.create(
            photo="media/food.svg",
            title="test2",
            carbohydrates=0.0,
            protein=0.0,
            fats=0.0,
            price=0.0,
            ingredients="test test test",
            calories=0.0,
            kcal=0.0,
        )
        data.save()

    # def test_short_fit_list(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create your tests here.
