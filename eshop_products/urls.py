from django.contrib import admin
from django.urls import path, include

from eshop_products.views import ProductList, SearchProduct, product_detail, ProductListByCategory, \
    product_categories_partial,like_post

urlpatterns = [
    path('products/', ProductList.as_view(), name='productlist'),
    path('products/<product_id>/<slug>' ,product_detail , name='productdetail' ) ,
    path('products/search', SearchProduct.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view(),name='product_by_category'),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial'),
    path('like_post/<int:pk>', like_post , name='like_post'),
]
