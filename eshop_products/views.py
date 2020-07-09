from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.


class ProductList(ListView):
    queryset = Product.objects.get_active_product()
    template_name = 'products/product_list.html'
    paginate_by = 3

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data(*args, **kwargs)
        return context


class ProductDetail(DetailView):
    queryset = Product.objects.get_active_product()
    template_name = 'products/product_detail.html'

