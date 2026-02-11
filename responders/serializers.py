from rest_framework import serializers
from .models import ResponderTeam

class ResponderTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderTeam
        fields = ['id', 'team_name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']