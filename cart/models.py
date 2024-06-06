from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here.
class Cart(models.Model):
    customUser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.customUser, self.product, self.quantity 
    
    
    
    
    
    
class Order(models.Model):
    customUser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customUser, self.product, self.quantity 