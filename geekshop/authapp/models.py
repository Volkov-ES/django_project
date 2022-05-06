from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="user_images", blank=True)

