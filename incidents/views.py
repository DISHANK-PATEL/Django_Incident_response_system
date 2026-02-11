from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentReportSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class IncidentViewSet(viewsets.ModelViewSet):
    """
    This ViewSet handles:
    - GET /api/incidents/reports/ (List all)
    - POST /api/incidents/reports/ (Create new)
    - GET /api/incidents/reports/{id}/ (Detail)
    """
    queryset = Incident.objects.all().order_by('-created_at')
    serializer_class = IncidentReportSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)