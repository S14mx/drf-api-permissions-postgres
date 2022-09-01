from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Car


class CarTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='test_user', password='pass')
        test_user.save()

        test_car = Car.objects.create(
            owner=test_user, make="Car2", model="A Car", year=2018, mpg=20)
        test_car.save()

    def test_Cars_model(self):
        car = Car.objects.get(id=1)
        actual_owner = str(car.owner)
        actual_make = str(car.make)
        actual_model = str(car.model)
        self.assertEqual(actual_owner, "test_user")
        self.assertEqual(actual_make, "Car2")
        self.assertEqual(actual_model, "A Car")
