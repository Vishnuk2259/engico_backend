from django.db import models
from django.utils import timezone
from datetime import datetime
from shared.models import BaseModel

class Banner(BaseModel):
    page_url = models.CharField(max_length = 255, null = True, blank = True)
    banner_type = models.CharField(max_length = 100, choices=[('Header', 'Header'), ('Footer', 'Footer')], null = True, blank = True)
    content = models.TextField(max_length = 500, null = True, blank = True)
    file = models.CharField(max_length = 255, null = True, blank = True)
    file_type = models.CharField(max_length = 50, null = True, blank = True)
    title = models.CharField(max_length = 255, null = True, blank = True)
    
    def __str__(self):
        return f"{self.content} , {self.id}"