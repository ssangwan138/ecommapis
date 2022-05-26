from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=15)
    product_desc = models.CharField(max_length=50)
    category = models.CharField(max_length=15, default="")
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
