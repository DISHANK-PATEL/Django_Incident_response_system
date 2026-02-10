from django.test import TestCase
from incidents.models import Incident
from django.contrib.auth import get_user_model

User = get_user_model()

class IncidentModelTests(TestCase):

    def test_incident_str_representation(self):
        user = User.objects.create_user(username='testuser')
        incident = Incident.objects.create(
            title="Fire",
            description="Small fire in trash can",
            category="SAFETY",
            severity="MEDIUM",
            location="Backyard",
            reported_by=user
        )
        self.assertEqual(str(incident), "Fire - OPEN")