from django.db import models


# Create your models here.

class GarageSellModel(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=1000, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.CharField(max_length=1000, default="")
