from django.db import models

import uuid

class productCategory(models.Model):
    category_name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    

    