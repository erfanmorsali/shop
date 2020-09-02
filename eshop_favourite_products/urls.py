from django.urls import path, include
from .views import FavouriteProducts, add_favourite_product

urlpatterns = [
    path('favourite-products', FavouriteProducts.as_view(),name='favourite-products'),
    path('add_favourite_product', add_favourite_product,name='add_favourite_product'),

]
