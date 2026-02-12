from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from incidents.models import Incident

User = get_user_model()

class MetricTests(APITestCase):
    def test_metrics_structure(self):
    
        user = User.objects.create_user(username='tester', password='pw')
        self.client.force_authenticate(user=user)
        
        past_time = timezone.now() - timedelta(hours=1)
        ack_time = timezone.now() - timedelta(minutes=30)
        
        Incident.objects.create(
            title="Test Incident",
            severity="HIGH",
            category="IT",
            reported_by=user, 
            created_at=past_time,
            acknowledged_at=ack_time 
        )

        url = reverse('incident-reports-get-metrics')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['avg_acknowledgement_time'], "N/A")