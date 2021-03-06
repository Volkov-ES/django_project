from email.mime import image
from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return f'(self.id): {self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=140, blank=True)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'(self.id): {self.name}'