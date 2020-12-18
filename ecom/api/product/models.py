from django.db import models
from django.db.models.fields import NullBooleanField
from api.category.models import Category


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_name_discription = models.CharField(max_length=250)
    product_price = models.CharField(max_length=50)
    product_stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name