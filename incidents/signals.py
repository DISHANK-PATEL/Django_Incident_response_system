from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Incident, IncidentStatusHistory

@receiver(pre_save, sender=Incident)
def log_status_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Incident.objects.get(pk=instance.pk)
            
            if old_instance.current_status != instance.current_status:
                
                user = getattr(instance, 'last_modified_by', None)
                
                IncidentStatusHistory.objects.create(
                    incident=instance,
                    old_status=old_instance.current_status,
                    new_status=instance.current_status,
                    changed_by=user 
                )
        except Incident.DoesNotExist:
            pass