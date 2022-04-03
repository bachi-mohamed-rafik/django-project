from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255 , blank=False , null=False)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL , null=True, blank=True) 
    def __str__(self):
        return self.name
        
