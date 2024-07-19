from authentication.models import User
from authentication.tests.test_setup import TestSetup

class TestViews(TestSetup):
    
    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register_correctly(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(self.user_data['email'], response.data['email'])
        self.assertEqual(response.status_code, 201)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 200)
