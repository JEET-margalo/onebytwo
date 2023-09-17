from django.db import models
import os
# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=30)
    Email= models.EmailField(max_length=254)
    phone= models.IntegerField(max_length=13)
    account = models.CharField(max_length=10)
    message = models.CharField(max_length=300)
   