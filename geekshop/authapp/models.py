from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, blank=True)