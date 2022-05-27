from asyncio.windows_events import NULL
from random import choices
from unicodedata import name
from django.db import models
from django.forms import CharField, ChoiceField

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=50,default='')
    details = models.CharField(max_length=500, default='', blank=True)
    def __str__(self):
        return self.name
    class Meta:
        #db_table = 'Supplier'
        # Add verbose name
        verbose_name = 'Supplier'


class Product(models.Model):
    def __str__(self):
        return self.name
    queryset = Supplier.objects.values_list('name', flat = True)
    name = models.CharField(max_length=50,default='')
    price = models.FloatField(default = '')
    details = models.CharField(max_length=500, default='', blank= True)
    #supplier = models.CharField(max_length=50,default=NULL)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=NULL)

class Grades(models.Model):
    def __str__(self):
        return self.user
    chargrade = models.CharField(max_length= 1000)
    user = models.CharField(max_length= 100)