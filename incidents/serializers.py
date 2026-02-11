from rest_framework import serializers
from .models import Incident
from responders.models import ResponderTeam

class IncidentReportSerializer(serializers.ModelSerializer):
    
    assigned_team_name = serializers.CharField(source='assigned_team.team_name', read_only=True)
    attachment = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = Incident
        fields = [
            'id', 'title', 'description', 'category', 'severity', 
            'location', 'current_status', 'assigned_team', 
            'assigned_team_name',  
            'attachment',         
            'reported_by'
        ]
        read_only_fields = ['reported_by', 'assigned_team_name']

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