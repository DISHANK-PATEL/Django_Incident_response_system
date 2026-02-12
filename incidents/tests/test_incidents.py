from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from incidents.models import Incident, IncidentStatusHistory
from responders.models import ResponderTeam

User = get_user_model()

class IncidentCoreTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin_test', password='pw', role='ADMIN')
        self.client.force_authenticate(user=self.admin)
        self.team = ResponderTeam.objects.create(team_name="SRE") 
        
        self.incident = Incident.objects.create(
            title="DB Spike", 
            category="IT", 
            severity="HIGH", 
            current_status="OPEN",
            reported_by=self.admin 
        )

    def test_atomic_signal_and_sla(self):
    
        url = reverse('incident-reports-detail', kwargs={'pk': self.incident.id})
        
        response = self.client.patch(url, {"current_status": "ACKNOWLEDGED", "assigned_team": self.team.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.incident.refresh_from_db()
        self.assertIsNotNone(self.incident.acknowledged_at) 
        self.assertEqual(IncidentStatusHistory.objects.count(), 1) 

    def test_advanced_queries(self):
        """Tests Filtering and Sorting using actual ViewSet method names"""
    
        Incident.objects.create(
            title="Critical Latency", 
            severity="CRITICAL", 
            category="IT",
            reported_by=self.admin
        )

        Incident.objects.create(
            title="Minor Bug", 
            severity="LOW", 
            category="IT",
            reported_by=self.admin
        )
        
    
        sort_url = reverse('incident-reports-sort-severity')
        response = self.client.get(sort_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data[0]['severity'], "CRITICAL") 
        
        self.assertEqual(response.data[1]['severity'], "HIGH")
        
        self.assertEqual(response.data[-1]['severity'], "LOW")