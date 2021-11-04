from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discounted_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=500)

class Order(models.Model):
    items=models.CharField(max_length=900)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    total=models.CharField(max_length=500)