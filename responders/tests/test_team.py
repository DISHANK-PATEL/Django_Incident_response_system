from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from responders.models import ResponderTeam

User = get_user_model()

class TeamTests(APITestCase):
    def setUp(self):

        self.admin = User.objects.create_user(username='team_admin', password='pw', role='ADMIN')
        self.client.force_authenticate(user=self.admin)
        

        self.team = ResponderTeam.objects.create(team_name="DevOps")

    def test_team_creation(self):
        """Verifies that a new responder team can be created via POST"""
    
        url = reverse('responder-teams-list') 
        data = {"team_name": "SRE", "on_call_status": True}
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResponderTeam.objects.count(), 2)
        self.assertEqual(response.data['team_name'], "SRE")

    def test_team_patching(self):
        """Verifies partial update of a team name via PATCH"""
    
        url = reverse('responder-teams-detail', kwargs={'pk': self.team.id})
        data = {"team_name": "Platform Engineering"}
        
        response = self.client.patch(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.team_name, "Platform Engineering")