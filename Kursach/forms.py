from unicodedata import name
from django import forms

from Kursach.models import Supplier


class RegForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=40, label="Введите логин")
    password1 = forms.CharField(min_length=5, max_length=30, widget = forms.PasswordInput, label="Введите пароль")
    password2 = forms.CharField(min_length=5, max_length=30, widget = forms.PasswordInput, label="Повторите пароль")

class LogForm(forms.Form):
    username = forms.CharField(min_length=2, max_length=40, label="Введите логин")
    password = forms.CharField(min_length=5, max_length=30, widget=forms.PasswordInput, label="Введите пароль")

class ProductForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, label="Введите название товара")
    price = forms.FloatField(label="Введите цену")
    details = forms.CharField(max_length=500, label="Введите доп. информацию")
    supplier = forms.ModelChoiceField(queryset = Supplier.objects.values_list('name', flat = True))

class SupplierForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, label="Введите название постващика")
    details = forms.CharField(max_length=500, label="Введите доп. информацию")

class FilterForm(forms.Form):
    min = forms.FloatField (label="Минимальная стоимость")
    max = forms.FloatField (label="Максимальная стоимость")

class SupplierSearchForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, label="Введите название постващика")
    
class ProductNameSearchForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, label="Введите название товара")

class ProductPriceSearchForm(forms.Form):
    price = forms.FloatField(label="Введите цену")

class GradeForm(forms.Form):
    grade = forms.IntegerField(max_value=30, min_value=0, label="Оценка")

