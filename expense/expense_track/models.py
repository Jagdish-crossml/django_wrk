from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils import timezone
import datetime
# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.date.today)
    comment = models.CharField(max_length=200)
    CATEGORIES = [
		('Travel','Travel'),
		('Education','Education'),
		('Gifts & Donations','Gifts & Donations'),
		('Investments','Investments'),
		('Bills & Utilities','Bills & Utilities'),
		('Food & Dining','Food & Dining'),
		('Health & Fitness','Health & Fitness'),
		('Personal Care','Personal Care'),
		('Fees & Charges','Fees & Charges'),
		('Others','Others')
	]    
    category = models.CharField(max_length=200,choices=CATEGORIES,default='*')


    def __str__(self):
        return self.name

# class Category(models.Model):
#     cat_name = models.CharField(max_length=200)
#     expense = models.ForeignKey(Expense,on_delete=CASCADE)
    

#     def __str__(self):
#         return self.cat_name

                          