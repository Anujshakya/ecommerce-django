from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'image')
    
# Register your models here.
admin.site.register(Product, ProductAdmin)