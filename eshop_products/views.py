import itertools

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductGallery
from django.http import Http404
from eshop_products_category.models import ProductCategory


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


def product_detail(request, *args, **kwargs):
    product_id = kwargs['product_id']
    slug = kwargs['slug']
    product = Product.objects.get_product_by_id(product_id, slug)

    if product is None:
        raise Http404('محصولی با این مشخصات یافت نشد')

    galeries = ProductGallery.objects.filter(product_id=product_id)
    grouped_galeries = list(my_grouper(3 , galeries))

    related_products = Product.objects.get_queryset().filter(category__product=product).distinct()
    grouped_related_products = list(my_grouper(3,related_products))

    context = {
        'product': product,
        'galeries' : grouped_galeries ,
        'related_products' : grouped_related_products
    }
    return render(request, 'products/product_detail.html', context)


class SearchProduct(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

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
