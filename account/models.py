from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    
    user_type = models.CharField(max_length=200,
        choices=[
        ('admin','Admin'),
        ('salesofficer','Salesofficer'),
        ('callcenter','Callcenter')
        ]
        )
    
    REQUIRED_FIELDS = []