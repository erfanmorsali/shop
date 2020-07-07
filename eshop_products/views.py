from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.


class ProductList(ListView):
    queryset = Product.objects.get_active_product()
    template_name = 'products/product_list.html'


class ProductDetail(DetailView):
    queryset = Product.objects.get_active_product()
    template_name = 'products/product_detail.html'


