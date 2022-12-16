from django.db import models


# Create your models here.

class Products(models.Model):
    image = models.ImageField(blank=True, null=True)
    product = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)
    price = models.FloatField()
