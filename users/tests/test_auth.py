from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register') 
        self.login_url = reverse('token_obtain_pair')
        self.user_data = {
            "username": "responder_one",
            "password": "securepassword123",
            "role": "RESPONDER",
            "email": "responder@company.com"
        }

    def test_registration_and_jwt_flow(self):
       
        reg_response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(reg_response.status_code, status.HTTP_201_CREATED)
        
        login_data = {"username": "responder_one", "password": "securepassword123"}
        login_response = self.client.post(self.login_url, login_data)
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', login_response.data)