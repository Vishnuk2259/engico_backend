from django.db import models
from shared.models import BaseModel

class Feedback(BaseModel):
    content = models.TextField(max_length = 500, null = True, blank = True)
    client_name = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.client_name
