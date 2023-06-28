from django.db import models
from products.models import Product


class Order(models.Model):
    products = models.ManyToManyField(Product) # through='Product_owner'
    number = models.IntegerField()
    status = models.CharField(max_length=2)
    timestamp = models.DateTimeField()


# class Product_owner(models.Model):
#     product = models.ForeignKey(Product)
#     order = models.ForeignKey(Order)

class table(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=250)


class Receipt(models.Model):
    orders = models.ForeignKey('Order', on_delete=models.PROTECT)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    final_price = models.DecimalField(decimal_places=2, max_digits=8)