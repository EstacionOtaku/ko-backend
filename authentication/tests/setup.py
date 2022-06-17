from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_endpoint = reverse('register')
        self.login_endpoint = reverse('login')

        self.faker = Faker()
        self.email = self.faker.email()
        self.username = self.email.split('@')[0]
        # garyrodriguez@example.org
        # ['garyrodriguez', 'example.org']
        self.password = self.username
        self.password_confirmation = self.password

        self.data = {
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'password_confirmation': self.password_confirmation
        }

    def tearDown(self):
        return super().tearDown()
