from django.contrib import admin
from django.urls import path, include

from eshop_products.views import ProductList, SearchProduct, ProductDetail, ProductListByCategory, \
    product_categories_partial

urlpatterns = [
    path('products/', ProductList.as_view(), name='productlist'),
    path('products/<slug>', ProductDetail.as_view(), name='productdetail'),
    path('products/list/search', SearchProduct.as_view()),
    path('products/categories/<category_name>', ProductListByCategory.as_view()),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial'),

]
