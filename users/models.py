from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  
   
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        RESPONDER = 'RESPONDER', 'Responder'
        USER = 'USER', 'Standard User'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"