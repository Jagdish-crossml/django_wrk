from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils import timezone
# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    expense = models.ForeignKey(Expense,on_delete=CASCADE)
    

    def __str__(self):
        return self.cat_name

                          