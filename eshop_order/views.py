from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import Http404
from eshop_products.models import Product
from .forms import UserAddOrder
from .models import Order, OrderDetail
from django.contrib import messages


# Create your views here.
@login_required(login_url='/login')
def add_user_order(request):
    new_order_form = UserAddOrder(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
        product_id = new_order_form.cleaned_data.get('productId')
        size = new_order_form.cleaned_data.get('size')
        color = new_order_form.cleaned_data.get('color')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.filter(id=product_id, attribute__size=size, attribute__color=color,
                                         active=True).first()
        if product is None:
            raise Http404("محصولی با این مضخصات یافت نشد")
        order.orderdetail_set.create(product_id=product.id, price=product.price, color=color, size=size,
                                     count=count)
        messages.success(request, 'محصول با موفقیت به سبد خرید اضافه شد')
        return redirect(f'/products/{product.id}/{product.slug}')


@login_required(login_url='/login')
def delete_user_order(request, *args,**kwargs):
    item_id = kwargs['item_id']
    OrderDetail.objects.filter(id=item_id).delete()
    return redirect('/order-items')


@login_required(login_url='/login')
def user_order_items(request):
    user_id = request.user.id
    order = Order.objects.filter(owner_id=user_id, is_paid=False).first()
    if order is None:
        raise Http404('کاربر هیچ محصولی در سبد خرید ندارد')
    order_items = OrderDetail.objects.all().filter(order=order)
    context = {
        "order": order_items
    }
    return render(request, 'order/user_order_detail.html', context)
