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
    

    