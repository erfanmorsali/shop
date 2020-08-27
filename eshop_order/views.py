from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from eshop_products.models import Product
from .forms import UserAddOrder
from .models import Order


# Create your views here.
@login_required()
def add_user_order(request):
    new_order_form = UserAddOrder(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
        product_id = new_order_form.cleaned_data.get('productId')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.filter(id=product_id).first()
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        print(order)
    return redirect('/products')
