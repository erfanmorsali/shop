import itertools
from eshop_favourite_products.forms import UserFavouriteProductForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from eshop_products_attrebute.models import ProductAttribute
from eshop_order.forms import UserAddOrder
from .forms import CommentForm
from .models import Product, ProductGallery, ProductComment
from django.http import Http404
from eshop_products_category.models import ProductCategory
from django.contrib import messages

# Create your views here.


class ProductList(ListView):
    queryset = Product.objects.get_active_product()
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data(*args, **kwargs)
        return context


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def like_post(request,pk):
    product = Product.objects.get(id=pk)
    if product is None:
        return Http404("یافت نشد")
    product.likes.add(request.user)
    return redirect(f"/products/{product.id}/{product.slug}")


def product_detail(request, *args, **kwargs):
    product_id = kwargs['product_id']
    slug = kwargs['slug']
    product = Product.objects.get_product_detail(product_id, slug)
    attribute = ProductAttribute.objects.filter(product=product)
    product_attrs = [attr for attr in attribute]



    if product is None:
        raise Http404('محصولی با این مشخصات یافت نشد')

    galeries = ProductGallery.objects.filter(product_id=product_id)
    grouped_galeries = list(my_grouper(3, galeries))

    related_products = Product.objects.get_queryset().filter(category__product=product).distinct()
    grouped_related_products = list(my_grouper(3, related_products))
    new_order_form = UserAddOrder(request.POST or None, initial={'productId': product_id})
    UserFavouriteForm = UserFavouriteProductForm(request.POST or None, initial={'productId': product_id})
    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid():
        full_name = comment_form.cleaned_data.get('full_name')
        email = comment_form.cleaned_data.get('email')
        message = comment_form.cleaned_data.get('message')
        ProductComment.objects.create(full_name=full_name, email=email, message=message, product=product)
        messages.success(request,"نظر شما با موفقیت ثبت شد")

    message = messages.get_messages(request)
    context = {
        'product': product,
        'galeries': grouped_galeries,
        'related_products': grouped_related_products,
        'comment_form': comment_form,
        'new_order_form': new_order_form,
        'product_attrs': product_attrs,
        'UserFavouriteForm': UserFavouriteForm,
        'messages' : message,
    }

    return render(request, 'products/product_detail.html', context)


class SearchProduct(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 2

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_product()


class ProductListByCategory(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        else:
            return Product.objects.get_product_by_category(category_name)


def product_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/product_categories_partial.html', context)
