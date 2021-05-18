from django.conf import settings
from django.db import models
from django.utils import timezone

class Room(models.Model):
    location = models.CharField(max_length=150)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
class Car(models.Model):
    identifier = models.CharField(max_length=8)
    desc = models.TextField(blank=True, null=True)
    drivers = models.CharField(max_length=100)