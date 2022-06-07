from asyncio.windows_events import NULL
from contextlib import suppress
from dataclasses import dataclass
from distutils.log import Log
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from Kursach.models import Grades, Product, Supplier
from .forms import FilterForm, GradeForm, ProductNameSearchForm, ProductPriceSearchForm, RegForm, LogForm, SupplierForm, ProductForm, SupplierSearchForm
from django.contrib.auth.decorators import login_required

import numpy as np
import json


class Funcs():
    def filterProdPrice(self):
        pass

    def sortSupName(self):
        pass

    def sortProdName(self):
        pass

    def sortProdPrice(self):
        pass


def index(request):
    user = request.user.username
    data = {'username': user}
    return render(request, 'index.html', context=data)


def register(request):

    form = RegForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                 return redirect ('register')
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save()
                return redirect ('login')
        else: 
            return redirect ('register')
    else:
        return render(request, 'register.html', {'form': form})

def login(request):
    form = LogForm()
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = auth.authenticate(username=username, password=password)
         if user is not None:
             auth.login(request, user)
             return redirect('')
         else:
            return redirect ('login')
    else: 
        return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('')

@login_required(login_url='login')
def view_suppliers(request):
    if request.method =="POST":
        pass
    else:
        sups = Supplier.objects.all()
        prods = Product.objects.all()
        data = {"sups":sups, "prods":prods}
        return render(request, 'view_suppliers.html', context=data)


class SortFuncs(Funcs):
    def sortSupName(self):
        sups = Supplier.objects.order_by('name')
        return sups
    def sortProdName(self):
        prods = Product.objects.order_by('name')
        return prods

    def sortProdPrice(self):
        prods = Product.objects.order_by('price')
        return prods


class FilterFuncs(Funcs):
    def filterProdPrice(self, min , max):
        sups = list(Supplier.objects.all())
        sups2 = list(Supplier.objects.all())
        prods = Product.objects.all()
        filtered_prods = list()
        min = float(min)
        max = float(max)
        for i in prods:
            if(i.price > min and i.price < max):
                filtered_prods.append(i)
        for i in sups:
            flag = 0
            for j in filtered_prods:
                if(i.name == j.supplier.name):
                    flag = 1
            if(flag == 0):
                sups2.remove(i)
        data = {"sups":sups2, "prods":filtered_prods}
        return data

@login_required(login_url='login')        
def view_sorted_supplier_name(request):
    if request.method =="POST":
        pass
    else:
       # sups = Supplier.objects.order_by('name')
        sups2 = SortFuncs()
        sups = sups2.sortSupName()
        prods = Product.objects.all()
        data = {"sups":sups, "prods":prods}
        return render(request, 'view_suppliers.html', context=data)

@login_required(login_url='login')        
def view_sorted_product_name(request):
    if request.method =="POST":
        pass
    else:
        sups = Supplier.objects.all()
        #prods = Product.objects.order_by('name')
        prods2 = SortFuncs()
        prods = prods2.sortProdName()
        data = {"sups":sups, "prods":prods}
        return render(request, 'view_suppliers.html', context=data)

@login_required(login_url='login')
def view_sorted_product_price(request):
    if request.method =="POST":
        pass
    else:
        sups = Supplier.objects.all()
       # prods = Product.objects.order_by('price')
        prods2 = SortFuncs()
        prods = prods2.sortProdName()
        data = {"sups":sups, "prods":prods}
        return render(request, 'view_suppliers.html', context=data)

@login_required(login_url='login')    
def view_filtered_product_price(request):
    if request.method =="POST":
        # sups = list(Supplier.objects.all())
        # sups2 = list(Supplier.objects.all())
        # prods = Product.objects.all()
        # filtered_prods = list()
        # min = request.POST["min"]
        # max = request.POST["max"]
        # min = float(min)
        # max = float(max)
        # for i in prods:
        #     if(i.price > min and i.price < max):
        #         filtered_prods.append(i)
        # for i in sups:
        #     flag = 0
        #     for j in filtered_prods:
        #         if(i.name == j.supplier.name):
        #             flag = 1
        #     if(flag == 0):
        #         sups2.remove(i)
        min = request.POST["min"]
        max = request.POST["max"]
        func = FilterFuncs()
        #data = {"sups":sups2, "prods":filtered_prods}
        data = func.filterProdPrice(min,max)
        return render(request, 'view_suppliers.html', context=data)
    else:
        form = FilterForm()
        data = {"form": form}
        return render(request, 'filter_suppliers.html', context=data)

@login_required(login_url='login')
def search(request):
    if request.method =="POST":
        pass
    else:
        data = {}
        return render(request, 'search.html', context=data)

@login_required(login_url='login')
def search_supplier(request):
    if request.method =="POST":
        prods = Product.objects.all()
        name = request.POST["name"]
        sups = Supplier.objects.filter(name = name)
        data = {"sups":sups, "prods":prods}
        return render(request, 'search.html', context=data)
    else:
        form = SupplierSearchForm()
        data = {"form":form}
        return render(request, 'search_supplier.html', context=data)

@login_required(login_url='login')
def search_product_name(request):
    if request.method =="POST":
        name = request.POST["name"]
        prods = Product.objects.filter(name=name)
        sups = Supplier.objects.all()
        sups2 = list()
        for i in prods:
            for j in sups:
                if(i.supplier.name == j.name):
                    sups2.append(j)
        data = {"sups":sups2, "prods":prods}
        return render(request, 'search.html', context=data)
    else:
        form = ProductNameSearchForm()
        data = {"form":form}
        return render(request, 'search_product_name.html', context=data)

@login_required(login_url='login')
def search_product_price(request):
    if request.method =="POST":
        price = request.POST["price"]
        price = float(price)
        prods = Product.objects.filter(price=price)
        sups = Supplier.objects.all()
        sups2 = list()
        for i in prods:
            for j in sups:
                if(i.supplier.name == j.name):
                    sups2.append(j)
        
        data = {"sups":sups2, "prods":prods}
        return render(request, 'search.html', context=data)
    else:
        form =ProductPriceSearchForm()
        data = {"form":form}
        return render(request, 'search_product_price.html', context=data)
"""
arr=[
    [1,2,3,4]
    [1,2,3,4]
    [1,2,3,4]
    [1,2,3,4]
]
"""
arr = []
arrstr = []
iter = [0, 1]
@login_required(login_url='login')
def grade(request):
    supAmount= Supplier.objects.count()
    sups = Supplier.objects.all()
    prods = Product.objects.all()
    if supAmount < 2:
        return redirect('')
    if request.method =="POST":
        cell = request.POST["grade"]
        cell = int(cell)
        arr[iter[0]][iter[1]] = cell
        arr[iter[1]][iter[0]] = 30 - cell
        iter[0]= iter[0] + 1
        if iter[0] == iter[1]:
            iter[0] = 0
            iter[1]= iter[1] + 1
        if iter[1]==supAmount:
            jackson = json.dumps(arr, indent=4)
            user = request.user.username
            grades = Grades.objects.create(chargrade = jackson, user = user)
            gr = Grades.objects.all()
            for g in gr:
                if user == g.user:
                    g.delete()
            grades.save()
            return redirect('grade_view')
        iter0 = iter[0]
        iter1 = iter[1]
        sup1 = sups[iter[0]]
        sup2 = sups[iter[1]]
        form = GradeForm()
        data = {'form':form, 'sup1':sup1, 'sup2':sup2, "prods":prods, 'arr':arr}
        return render(request, 'grade.html', context=data)
    else:
        arr.clear()
        arrstr.clear()
        for ii in range(supAmount):
            arrstr.clear()
            for jj in range(supAmount):
                arrstr.append(0)
            buf = arrstr.copy()
            arr.append(buf)
        iter[1] = 1
        iter[0] = 0
        iter1 = 1
        iter0 = 0
        sup1 = sups[iter0]
        sup2 = sups[iter1]
        form = GradeForm()
        data = {'form':form, 'sup1':sup1, 'sup2':sup2, "prods":prods, 'arr':arr}
        return render(request, 'grade.html',context=data)

@login_required(login_url='login')
def grade_view(request):
    amount = Supplier.objects.count()
    amount = range(amount)
    data = {'arr':arr, 'amount':amount}
    return render(request, "grade_view.html", context=data)

@login_required(login_url='login')
def method(request):
    try:
        grades = Grades.objects.all()
        sups = Supplier.objects.count()
        sups2 = list(Supplier.objects.all())
        prods = Product.objects.all()
        mass =list()
        for i in range(sups):
            mark = 0
            for p in grades:
                buf = json.loads(p.chargrade)
                for w in range(sups):
                    mark = mark + buf[i][w]
            mass.append(mark)

        for i in range(sups-1):
            for j in range(sups-i-1):
                if mass[j] < mass[j+1]:
                    mass[j], mass[j+1] = mass[j+1], mass[j]
                    supbuf =sups2[j]
                    sups2[j] = sups2[j+1]
                    sups2[j+1] = supbuf


        data = {'sups':sups2,'prods':prods, 'mass':mass}
        return render(request, "method.html", context=data)
    except:
        print('Критическая ошибка')
