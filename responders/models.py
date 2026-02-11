from django.db import models
from django.conf import settings

class ResponderTeam(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
  
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name