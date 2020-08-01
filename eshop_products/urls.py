from django.contrib import admin
from django.urls import path, include

from eshop_products.views import ProductList, SearchProduct, product_detail, ProductListByCategory, \
    product_categories_partial

urlpatterns = [
    path('products/', ProductList.as_view(), name='productlist'),
    path('products/<product_id>/<slug>' ,product_detail , name='productdetail' ) ,
    path('products/search', SearchProduct.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial'),

]
