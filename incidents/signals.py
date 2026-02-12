from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Incident, IncidentStatusHistory

@receiver(pre_save, sender=Incident)
def handle_incident_updates(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Incident.objects.get(pk=instance.pk)
    
        if old_instance.current_status != instance.current_status:
            
            with transaction.atomic():
                IncidentStatusHistory.objects.create(
                    incident=instance,
                    old_status=old_instance.current_status,
                    new_status=instance.current_status,
                    changed_by=getattr(instance, '_status_changer', None)
                )

                if old_instance.current_status == 'OPEN' and instance.current_status == 'ACKNOWLEDGED':
                    if not instance.acknowledged_at: 
                        instance.acknowledged_at = timezone.now()
                
                if instance.current_status == 'RESOLVED':
                    if not instance.resolved_at:
                        instance.resolved_at = timezone.now()

    except Incident.DoesNotExist:
        pass
    except Exception as e:
        print(f"Error in signal: {e}")