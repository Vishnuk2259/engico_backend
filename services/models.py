from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null = True, blank = True)
    description = models.TextField(null = True, blank = True)