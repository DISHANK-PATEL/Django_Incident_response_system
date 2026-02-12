from django.db.models import Q, Case, When, Value, IntegerField
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Incident, IncidentStatusHistory, IncidentUpdate
from .serializers import (
    IncidentReportSerializer, 
    StatusHistorySerializer, 
    IncidentUpdateSerializer
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by('-created_at')
    serializer_class = IncidentReportSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return Incident.objects.all().order_by('-created_at')
        return Incident.objects.filter(reported_by=user).order_by('-created_at')
            
        return Incident.objects.filter(reported_by=user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(_status_changer=self.request.user)
    
    @action(detail=False, methods=['get'], url_path='unresolved')
    def unresolved(self, request):
        queryset = self.get_queryset().exclude(current_status='RESOLVED')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='filter')
    def filter_incidents(self, request):
        category = request.query_params.get('category')
        location = request.query_params.get('location')
        queryset = self.get_queryset()
        
        if category:
            queryset = queryset.filter(category=category)
        if location:
            queryset = queryset.filter(location__icontains=location)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='sort-severity')
    def sort_severity(self, request):
        queryset = self.get_queryset().annotate(
            priority=Case(
                When(severity='CRITICAL', then=Value(4)),
                When(severity='HIGH', then=Value(3)),
                When(severity='MEDIUM', then=Value(2)),
                When(severity='LOW', then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by('-priority', '-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    

    @action(detail=True, methods=['post'], url_path='updates')
    def add_update(self, request, pk=None):
        incident = self.get_object()
        serializer = IncidentUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(incident=incident, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='timeline')
    def get_timeline(self, request, pk=None):
        incident = self.get_object()
        
        history = StatusHistorySerializer(incident.status_history.all(), many=True).data
        for h in history: h['event_type'] = 'AUDIT_LOG'

        updates = IncidentUpdateSerializer(incident.official_updates.all(), many=True).data
        for u in updates: u['event_type'] = 'OFFICIAL_UPDATE'

        timeline = sorted(history + updates, key=lambda x: x['created_at'], reverse=True)
        return Response(timeline)