from rest_framework import viewsets, permissions
from .models import ResponderTeam
from .serializers import ResponderTeamSerializer

class ResponderTeamViewSet(viewsets.ModelViewSet):
    """
    Handles:
    - POST /api/incidents/teams/ (Create a team)
    - GET /api/incidents/teams/ (List all teams)
    """
    queryset = ResponderTeam.objects.all()
    serializer_class = ResponderTeamSerializer
    permission_classes = [permissions.IsAuthenticated]