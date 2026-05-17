from django.db import models
from datetime import datetime
# Create your models here.

# Room model to represent a chat room
class Room(models.Model):
    name = models.CharField(max_length=255)

# Message model to represent a chat message
class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.TextField()
    room = models.TextField()