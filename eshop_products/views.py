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


class ProductDetail(DetailView):
    template_name = 'products/product_detail.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        product = Product.objects.filter(active=True, id=pk, slug=slug)
        if product is not None:
            return product
        else:
            raise Http404('محصول مورد نظر یافت نشد')

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product_id = self.kwargs['pk']
        galleries = ProductGallery.objects.filter(product_id=product_id)
        grouped_galleries = list(my_grouper(3 , galleries))
        print(grouped_galleries)

        context['galleries'] = grouped_galleries
        return context


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
