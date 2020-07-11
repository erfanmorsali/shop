from django.contrib import admin
from django.urls import path, include

from eshop_products.views import ProductList, SearchProduct , ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='productlist'),
    path('products/<slug>', ProductDetail.as_view(), name='productdetail'),
    path('products/list/search', SearchProduct.as_view()),

]
