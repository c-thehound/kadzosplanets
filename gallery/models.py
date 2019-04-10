from django.db import models
import datetime

class Image(models.Model):
    image = models.ImageField()
    description = models.TextField()
    uploaded = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.description

