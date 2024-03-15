from django.db import models
from django.utils import timezone
from datetime import datetime

from django.db import models
from shared.models import Brand
from shared.models import Category
from services.models import Service
from shared.models import BaseModel

class Product(BaseModel):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True)
    service = models.ForeignKey(Service, on_delete = models.CASCADE, null = True, blank = True)
    product_title = models.CharField(max_length = 255, null = True, blank = True)
    subtitle = models.CharField(max_length = 255, null = True, blank = True)
    description = models.TextField(max_length = 500, null = True, blank = True)
    meta_slug = models.CharField(max_length = 255, null = True, blank = True)
    meta_title = models.CharField(max_length = 255, null = True, blank = True)
    meta_description = models.TextField(max_length = 500, null = True, blank = True)
    meta_keywords = models.TextField(max_length = 500, null = True, blank = True)
    meta_image = models.ImageField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.product_title}"