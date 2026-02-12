from rest_framework import serializers
from .models import Incident, IncidentUpdate, IncidentStatusHistory
from responders.models import ResponderTeam

class IncidentReportSerializer(serializers.ModelSerializer):
    assigned_team_name = serializers.CharField(source='assigned_team.team_name', read_only=True)
    attachment = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
       
        model = Incident
        fields = [
            'id', 'title', 'description', 'category', 'severity', 
            'location', 'current_status', 'assigned_team', 
            'assigned_team_name', 'attachment', 'reported_by'
        ]
        read_only_fields = ['reported_by', 'assigned_team_name']

    def validate(self, data):
        request = self.context.get('request')
        instance = self.instance  
        new_status = data.get('current_status')
        new_team = data.get('assigned_team')

        if request and request.user.role == 'USER' and new_team:
            raise serializers.ValidationError(
                {"assigned_team": "Only Admins can assign responder teams."}
            )

        if instance:  
            status_order = {
                'OPEN': ['ACKNOWLEDGED'],
                'ACKNOWLEDGED': ['IN_PROGRESS'],
                'IN_PROGRESS': ['RESOLVED'],
                'RESOLVED': []  
            }

            if new_status and new_status != instance.current_status:
                allowed_next_steps = status_order.get(instance.current_status, [])
                
                if new_status not in allowed_next_steps:
                    raise serializers.ValidationError({
                        "current_status": f"Invalid move. From {instance.current_status}, you can only go to {allowed_next_steps}."
                    })

                if new_status == 'ACKNOWLEDGED' and not new_team and not instance.assigned_team:
                    raise serializers.ValidationError({
                        "assigned_team": "A responder team must be assigned before acknowledging."
                    })

        return data

class IncidentUpdateSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = IncidentUpdate
        fields = ['id', 'author_name', 'message', 'created_at']

class StatusHistorySerializer(serializers.ModelSerializer):
    changed_by_name = serializers.ReadOnlyField(source='changed_by.username')

    class Meta:
        model = IncidentStatusHistory
        fields = ['old_status', 'new_status', 'changed_by_name', 'created_at']