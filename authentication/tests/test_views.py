from .setup import TestSetUp
from rest_framework import status
from authentication.models import User


class TestViews(TestSetUp):
    def testUserRegisterWithoutData(self):
        response = self.client.post(self.register_endpoint)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testUserRegisterWithData(self):
        response = self.client.post(
            self.register_endpoint, self.data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.data['email'])
        self.assertEqual(response.data['username'], self.data['username'])

    def testUserLoginWithoutData(self):
        response = self.client.post(self.login_endpoint)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testUserLoginWithData(self):
        self.client.post(
            self.register_endpoint, self.data, format='json'
        )
        response = self.client.post(
            self.login_endpoint, {
                'email': self.data['email'],
                'password': self.data['password']
            }, format='json'
        )
        tokens = response.data['tokens']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', tokens)
        self.assertIn('refresh_token', tokens)

    def testRefreshTokenWithoutToken(self):
        pass

    def testRefreshTokenWithToken(self):
        pass
