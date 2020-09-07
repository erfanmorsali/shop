from eshop_products.models import Product
from django.shortcuts import render, Http404, redirect
from django.views.generic import ListView, DetailView
from .forms import UserFavouriteProductForm
from .models import UserFavouriteProducts
from django.contrib.auth.decorators import login_required


# Create your views here.


class FavouriteProducts(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        user_id = self.request.user.id
        prodcut = UserFavouriteProducts.objects.filter(owner_id=user_id).first()
        print(prodcut)
        if prodcut is None:
            return Product.objects.filter(active=True,userfavouriteproducts__owner_id=user_id)
        return Product.objects.filter(userfavouriteproducts__owner_id=user_id).distinct()


@login_required(login_url='/login')
def add_favourite_product(request):
    UserFavouriteProductsForm = UserFavouriteProductForm(request.POST or None)
    if UserFavouriteProductsForm.is_valid():
        productId = UserFavouriteProductsForm.cleaned_data.get('productId')
        product = Product.objects.filter(id=productId).first()
        if product is None:
            raise Http404('محصولی با این مشخصات یافت نشد')
        UserFavouriteProducts.objects.create(owner_id=request.user.id, product_id=product.id)
    return redirect('/products')
