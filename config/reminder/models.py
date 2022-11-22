from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz

class Reminders(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length = 300, blank=False, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_com = models.DateTimeField(blank=True, null=True)
    is_sent = models.BooleanField(default=False)
    is_marked = models.BooleanField(default=False)
    
    def date_due(self):
        s = (self.date_com - self.date_pub).total_seconds()
        days = s // 86400
        s = s - (days * 86400)
        hours = s // 3600 
        s = s - (hours * 3600)
        minutes = s // 60
        return f'{int(days)} days / {int(hours)} hours / {int(minutes)} minutes'
    
    def is_completed(self):
        if self.date_com <= datetime.datetime.utcnow().replace(tzinfo=pytz.UTC): return True
        return False
    
    def should_sent(self):
        result = (self.date_com - self.date_pub)
        
        if result <= datetime.timedelta(days=1): return True
        return False

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_pub']
