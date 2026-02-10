from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from incidents.models import Incident
from rest_framework_simplejwt.tokens import RefreshToken # <--- 1. Import this

User = get_user_model()

class IncidentAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='safety_officer', 
            password='securepassword123',
            role='USER'
        )
        self.url = reverse('incident-reports-list')
        

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_create_incident_authorized(self):
        """Test: A user with a valid JWT can report an incident."""
       
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        payload = {
            "title": "Gas Leak",
            "description": "Smell of gas in the cafeteria",
            "category": "SAFETY",
            "severity": "CRITICAL",
            "location": "Kitchen Area"
        }
        
        response = self.client.post(self.url, payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Incident.objects.count(), 1)
        self.assertEqual(Incident.objects.first().reported_by, self.user)