from django.db import models

class Store(models.Model):
  product_name = models.CharField(max_length=255)
  category_name = models.CharField(max_length=255)
  price = models.IntegerField(null=True)


