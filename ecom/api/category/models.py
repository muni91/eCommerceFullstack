from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_name_discription = models.CharField(max_length=250)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.category_name