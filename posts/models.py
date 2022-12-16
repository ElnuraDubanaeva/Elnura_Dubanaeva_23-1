from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    product = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)
    price = models.FloatField()


class Review(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="reviews")
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
