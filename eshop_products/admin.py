from django.contrib import admin
from .models import Product, ProductGallery
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.

def make_inactive(modeladmin, request, queryset):
    updated = queryset.update(active=False)
    modeladmin.message_user(request, ngettext(
        '%d محصول ناموجود شد.',
        '%d محصول ناموجود شدند.',
        updated,
    ) % updated, messages.SUCCESS)


make_inactive.short_description = "ناموجود کردن محصولات انتخاب شده"


def make_active(modeladmin, request, queryset):
    updated = queryset.update(active=True)
    modeladmin.message_user(request, ngettext(
        '%d محصول موجود شد.',
        '%d محصول موجود شدند.',
        updated,
    ) % updated, messages.SUCCESS)


make_active.short_description = "موجود کردن محصولات انتخاب شده"


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'slug', 'active']
    list_filter = ('timestamp', 'active')
    search_fields = ('title', 'description')
    actions = [make_inactive, make_active]

    class Meta:
        Model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
