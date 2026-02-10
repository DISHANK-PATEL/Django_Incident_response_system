from rest_framework import serializers
from .models import Incident
from responders.models import ResponderTeam

class IncidentReportSerializer(serializers.ModelSerializer):
    reported_by = serializers.ReadOnlyField(source='reported_by.username')
    
    assigned_team_name = serializers.ReadOnlyField(source='assigned_team.name')

    class Meta:
        model = Incident
        fields = [
            'id', 'title', 'description', 'category', 
            'severity', 'location', 'current_status', 
            'reported_by', 'assigned_team', 'assigned_team_name', 'created_at'
        ]

    def validate(self, data):
        """
        Even if the permission class allows the request, 
        the Serializer is the final checkpoint for data integrity.
        """
        request = self.context.get('request')
   
        if request and request.method == 'POST' and 'assigned_team' in data:
            if request.user.role == 'USER':
                raise serializers.ValidationError(
                    {"assigned_team": "Standard users cannot assign teams."}
                )
        return data