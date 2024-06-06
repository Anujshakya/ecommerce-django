from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/images/')
    category = models.CharField(max_length=150)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name