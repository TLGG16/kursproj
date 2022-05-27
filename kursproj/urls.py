"""kursproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Kursach import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name=''),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('view_suppliers/', views.view_suppliers, name='view_suppliers'),
    path('view_sorted_supplier_name', views.view_sorted_supplier_name, name='view_sorted_supplier_name'),
    path('view_sorted_product_name', views.view_sorted_product_name, name='view_sorted_product_name'),
    path('view_sorted_product_price', views.view_sorted_product_price, name='view_sorted_product_price'),
    path('filter_suppliers', views.view_filtered_product_price, name='view_filtered_product_price'),
    path('search', views.search, name='search'),
    path('search_supplier', views.search_supplier, name='search_supplier'),
    path('search_product_name', views.search_product_name, name='search_product_name'),
    path('search_product_price', views.search_product_price, name='search_product_price'),
    path('grade', views.grade, name='grade'),
    path('grade_view', views.grade_view, name='grade_view'),
    path('method', views.method, name='method'),
    #path('create_product/', views.create_product, name='create_product'),
    #path('create_supplier/', views.create_supplier, name='create_supplier'),
]
