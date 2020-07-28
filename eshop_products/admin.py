from django.contrib import admin
from .models import Product, ProductGallery


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'slug', 'active']

    class Meta:
        Model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
