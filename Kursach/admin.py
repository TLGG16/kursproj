from django.contrib import admin

from .models import Grades, Supplier, Product

# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Grades)