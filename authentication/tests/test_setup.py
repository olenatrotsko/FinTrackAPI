from django.urls import reverse

from rest_framework.test import APITestCase


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'email': 'email@gmail.com',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'password': 'password123',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    