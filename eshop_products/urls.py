from django.contrib import admin
from django.urls import path , include

from eshop_products.views import ProductList , ProductDetail

urlpatterns = [
    path('', ProductList.as_view() , name='productlist'),
    path('<slug>', ProductDetail.as_view() , name='productdetail'),

]