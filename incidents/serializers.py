from rest_framework import serializers
from .models import Incident

class IncidentReportSerializer(serializers.ModelSerializer):
    reported_by = serializers.ReadOnlyField(source='reported_by.username')

    class Meta:
        model = Incident
        fields = [
            'id', 'title', 'description', 'category', 
            'severity', 'location', 'current_status', 
            'reported_by', 'created_at'
        ]