from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.utils.html import format_html
from django.db.models import Q
from eshop_products_category.models import ProductCategory
from eshop_products_attrebute.models import ProductAttribute
from django.contrib.auth.models import User

# Create your models here.

class ProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_product_detail(self, product_id, slug):
        qs = self.get_queryset().filter(active=True, id=product_id, slug=slug)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)

        )
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)


class Product(models.Model):
    title = models.CharField(max_length=40, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='products/', null=True, verbose_name='تصویر')
    attribute = models.ManyToManyField(ProductAttribute,blank=True, verbose_name='مشخصات')
    slug = models.SlugField(unique=True, verbose_name='شناسه')
    active = models.BooleanField(default=False, verbose_name='موجود / ناموجود')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    category = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    likes = models.ManyToManyField(User, blank=True,verbose_name="لایک ها")

    objects = ProductManager()


    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'
        ordering = ['id']

    def thumbnail_pic(self):
        return format_html(f"<img  width=120 height=100 style='border-radius : 20px;' src={self.image.url} />")

    thumbnail_pic.short_description = 'تصویر'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(receiver=product_pre_save_receiver, sender=Product)


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to='products/galleries/', verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'تصاویر'
        verbose_name = 'تصویر'


class ProductComment(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='آدرس ایمیل ')
    message = models.TextField(verbose_name='نظر شما')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='محصول')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
