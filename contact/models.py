from django.db import models
from martor.models import MartorField
import datetime

class Subscriber(models.Model):
    email = models.EmailField(max_length=300,blank=True, null=True)
    date_subscribed = models.DateField(default=datetime.date.today)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Email(models.Model):
    subject = models.TextField()
    content = MartorField()

    def __str__(self):
        return self.subject