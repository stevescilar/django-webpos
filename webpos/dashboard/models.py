from tkinter import CASCADE
from django.db import models

import uuid

class productCategory(models.Model):
    category_name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_desc = models.CharField(max_length=200)
    item_price = models.FloatField(verbose_name='price')
    item_cat = models.ForeignKey(productCategory,verbose_name='category',on_delete=models.CASCADE)


    def __str__ (self):
        return self.item_name
    
#add to order for delivery
class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)
    order_item = models.ForeignKey(Item,on_delete=models.CASCADE)
    # ordered_by = models.ForeignKey(Customer,on_delete=models.CASCADE)
    # item_price = 

    def __str__ (self):
        return "%s" % (self.order_item)
    


    