from django.db import models
from django.utils import timezone
from datetime import datetime
from shared.models import BaseModel

class Service(BaseModel):
    service_name = models.CharField(max_length=255)
    title = models.CharField(max_length = 255, null = True, blank = True)
    subtitle = models.CharField(max_length = 255, null = True, blank = True)
    description = models.TextField(max_length = 500, null = True, blank = True)
    
    def __str__(self):
        return f"{self.service_name}"