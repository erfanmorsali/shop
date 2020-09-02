from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product
# Create your models here.


class UserFavouriteProducts(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "محصول مورد علاقه"
        verbose_name_plural = "محصولات مورد علاقه"