from django.db import models
import datetime
from martor.models import MartorField

class BlogPost(models.Model):
    title = models.CharField(max_length=500,blank=True, null=True)
    uploaded = models.DateField(default=datetime.date.today)
    updated = models.DateField(null=True,blank=True)
    content = MartorField()
    author = models.CharField(max_length=200,blank=True, null=True)
    snippet = models.TextField(blank=True,null=True)

    def get_snippet(self):
        text = self.content[0:150]
        return text+"..."  
    
    def save(self,*args,**kwargs):
        if not self.snippet:
            self.snippet = self.get_snippet()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title