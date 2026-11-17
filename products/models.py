from django.db import models

# Create your models here.

class category(models.Model):
    category_id=models.CharField(max_length=12)
    category_name=models.CharField(max_length=55)

    def __str__(self):
        return f"{self.category_name}"
    

class product(models.Model):
    product_id=models.CharField(max_length=12)
    product_name=models.CharField(max_length=55)
    stock=models.IntegerField()
    image=models.ImageField(upload_to="products")
    price=models.FloatField()
    features=models.TextField()

    def __str__(self):
        return f"{self.product_name}"    