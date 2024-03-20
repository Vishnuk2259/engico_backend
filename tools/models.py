from django.db import models
from shared.models import BaseModel

class Tools(BaseModel):
    content = models.TextField(max_length = 500, null = True, blank = True)
    file = models.FileField(null = True, blank = True)
    file_type = models.CharField(max_length = 50, null = True, blank = True)
    tool_name = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.tool_name

