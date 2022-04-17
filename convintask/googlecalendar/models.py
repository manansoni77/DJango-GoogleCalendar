from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_timestamp = models.DateTimeField('Timestamp')

    def __str__(self):
        return f"{self.event_name} at {self.event_timestamp}"
    
    def is_event_recent(self):
        return self.event_timestamp >= timezone.now() - datetime.timedelta(days=1)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_token = models.CharField(max_length=500)
