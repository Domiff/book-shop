from django.test import TestCase
from django.urls import reverse

from factories import User, make_login_credentials, make_register_credentials, make_user


class RegisterUserTest(TestCase):
    def setUp(self):
        self.credentials = make_register_credentials()

    def test_register(self):
        response = self.client.post(
            path=reverse("auth_user:register"), data=self.credentials
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)


class LoginUserTest(TestCase):
    def setUp(self):
        self.credentials = make_login_credentials()
        self.user = make_user(**self.credentials)

    def test_login(self):
        response = self.client.post(
            path=reverse("auth_user:login"), data=self.credentials
        )
        self.assertEqual(response.status_code, 302)
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)


class LogoutUserTest(TestCase):
    def setUp(self):
        self.user = make_user()

    def test_logout(self):
        response = self.client.post(path=reverse("auth_user:logout"))
        self.assertEqual(response.status_code, 302)
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)
