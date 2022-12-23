from django.contrib import admin
from posts.models import Product,Review,Categories

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Categories)