from django.urls import reverse

from faker import Faker
from rest_framework.test import APITestCase


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'first_name': self.fake.name().split()[0],
            'last_name': self.fake.name().split()[1],
            'password': self.fake.email(),
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    