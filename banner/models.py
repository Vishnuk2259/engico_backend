from django.db import models
from django.utils import timezone
from datetime import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        
    def strftime_created_at(self):
        return self.created_at.strftime("%d/%m/%Y, %H:%M:%S")
    
    def strftime_updated_at(self):
        return self.updated_at.strftime("%d/%m/%Y, %H:%M:%S")
    
    @classmethod
    def to_datetime(cls, timestamp):
        return datetime.fromtimestamp(timestamp)
    
    @classmethod 
    def to_timestamp(cls, time):
        return datetime.timestamp(time)
    
    def save(self, *args, **kwargs):
        if not self.id:  # Object is being created
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)
    
class Banner(BaseModel):
    page_url = models.CharField(max_length=255, null = True, blank = True)
    banner_type = models.CharField(max_length=10, choices=[('Header', 'Header'), ('Footer', 'Footer')], null = True, blank = True)
    content = models.TextField(null = True, blank = True)
    file = models.CharField(max_length=255, null = True, blank = True)
    file_type = models.CharField(max_length=50, null = True, blank = True)
    title = models.CharField(max_length=255, null = True, blank = True)
    
    def __str__(self):
        return f"{self.content} , {self.id}"