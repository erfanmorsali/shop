from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


# Create your models here.

class ProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=40, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='products/', null=True, verbose_name='تصویر')
    slug = models.SlugField(unique=True, blank=True, verbose_name='شناسه')
    active = models.BooleanField(default=False, verbose_name='موجود / ناموجود')
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, Product)
