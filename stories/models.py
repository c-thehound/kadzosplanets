from django.db import models
from martor.models import MartorField
import datetime

class Story(models.Model):
    title = models.CharField(max_length=500,blank=False)
    story_content = MartorField()
    uploaded = models.DateField(default=datetime.date.today)
    illustration = models.ImageField(upload_to="illustrations")
    
    def __str__(self):
        return self.title
