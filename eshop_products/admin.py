from django.contrib import admin
from .models import Product, ProductGallery, ProductComment
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.







class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'thumbnail_pic', 'price', 'slug', 'active']
    list_filter = ('timestamp', 'active')
    search_fields = ('title', 'description')
    list_editable = ['active']

    class Meta:
        Model = Product


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'product', 'is_read']
    list_editable = ['is_read']

    class Meta:
        Model = ProductComment


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(ProductComment, CommentAdmin)
