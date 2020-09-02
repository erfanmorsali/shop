from django.contrib import admin
from .models import UserFavouriteProducts


# Register your models here.

class FavouriteProductsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner']
    class Meta:
        Model = UserFavouriteProducts


admin.site.register(UserFavouriteProducts,FavouriteProductsAdmin)
