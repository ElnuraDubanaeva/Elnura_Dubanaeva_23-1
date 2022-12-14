from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=55)


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    price = models.FloatField()
    categories = models.ManyToManyField(Categories)
    reviewtable = models.BooleanField(default=True)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="reviews")
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
