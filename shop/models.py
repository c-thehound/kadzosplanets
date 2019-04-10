from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300,blank=False)
    description = models.TextField()
    price = models.IntegerField()
    amount_in_stock = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name

