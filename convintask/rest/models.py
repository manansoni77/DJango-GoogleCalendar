from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_timestamp = models.DateTimeField('Timestamp')

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_token = models.CharField(max_length=500)
