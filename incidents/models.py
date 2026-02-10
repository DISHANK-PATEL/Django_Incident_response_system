from django.db import models
from django.conf import settings
import uuid

class Incident(models.Model):
    
    class Severity(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
        CRITICAL = 'CRITICAL', 'Critical'

    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        ACKNOWLEDGED = 'ACKNOWLEDGED', 'Acknowledged'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        RESOLVED = 'RESOLVED', 'Resolved'

    class Category(models.TextChoices):
        SAFETY = 'SAFETY', 'Safety'
        IT = 'IT', 'IT Outage'
        FACILITY = 'FACILITY', 'Facility Breakdown'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=Category.choices)
    severity = models.CharField(max_length=20, choices=Severity.choices, default=Severity.LOW)
    location = models.CharField(max_length=255)
    
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reported_incidents')
    assigned_team = models.ForeignKey('responders.ResponderTeam', on_delete=models.SET_NULL, null=True, blank=True, related_name='incidents')
    
    current_status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.current_status}"