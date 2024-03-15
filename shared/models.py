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

class Settings(BaseModel):
    social_links = models.TextField(max_length = 255, null = True, blank = True)
    privacy = models.TextField(max_length = 255, null = True, blank = True)
    terms_and_conditions = models.TextField(max_length = 255, null = True, blank = True)
    policy = models.TextField(max_length = 255, null = True, blank = True)
    
    def __str__(self):
        return "Settings"
    

class ContactUs(BaseModel):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255, null = True, blank = True)
    email = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255, null = True, blank = True)
    subject = models.CharField(max_length = 255)
    company_name = models.CharField(max_length = 255, null = True, blank = True)
    job_title = models.CharField(max_length = 255, null = True, blank = True)
    comments = models.TextField(max_length = 500, null = True, blank = True)
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
    
    
class Category(BaseModel):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField(max_length = 500, null = True, blank = True)
    parent = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'subcategories')

    def __str__(self):
        return self.name

class Brand(BaseModel):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField(max_length = 500, null = True, blank = True)
    parent_brand = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'subbrands')

    def __str__(self):
        return self.name